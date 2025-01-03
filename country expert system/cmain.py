from bs4 import BeautifulSoup
from difflib import get_close_matches
import csv
from PIL import Image
import os

def select():
    """Displays the main menu."""
    while True:
        print("\nWelcome to the Geographic Information Expert System!")
        print("\t1. List the countries.")
        print("\t2. Search geographic details of a country.")
        print("\t3. See the country flag or map.")
        print("\t4. See exact location.")
        print("\t5. Expert system for living, working, or traveling suggestions.")
        print("\t6. Exit\n")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                list_countries()
            elif choice == 2:
                search_country_details()
            elif choice == 3:
                MaporFlag()
            elif choice == 4:
                seelocation()
            elif choice == 5:
                expert_system()
            elif choice == 6:
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

def list_countries():
    """Lists the countries available in the system."""
    try:
        with open("countryList.txt", "r") as file:
            countries = [line.strip()[3:].upper() for line in file]

        print("The countries you can search about are:")
        for idx, country in enumerate(countries, 1):
            print(f"{idx}. {country}")

    except FileNotFoundError:
        print("Error: 'countryList.txt' file not found.")
    

def MaporFlag():
    """Displays the flag or map of a country."""
    while True:
        choice = input("Do you want to see the flag or map? (type 'BACK' to return to the menu): ").strip().lower()
        
        if choice == 'back':
            return
        
        if choice not in ["flag", "map"]:
            print("Invalid choice. Please enter 'flag' or 'map'.")
            continue
        
        country = input("Enter a country (or type 'BACK' to return to the menu): ").strip()
        if country.lower() == 'back':
            return

        country = country.title()

        try:
            with open("countryList.txt", "r") as file:
                country_line = next((line for line in file if country in line), None)
            
            if not country_line:
                print("Country not found. Please try again.")
                continue

            page = country_line[:2].strip()
            display_map_or_flag(page, choice)
        
        except FileNotFoundError:
            print("Error: 'countryList.txt' file not found.")
            return

def display_map_or_flag(page, choice):
    """Displays the flag or map of the given country."""
    base_path = "graphics"
    folder = "flags/large" if choice == "flag" else "maps"
    file_name = f"{page}-{'lgflag' if choice == 'flag' else 'map'}.gif"
    file_path = os.path.join(base_path, folder, file_name)

    if not os.path.exists(file_path):
        print(f"Error: Could not find the {choice} for the page '{page}'.")
        return

    try:
        with Image.open(file_path) as img:
            img.show()
    except Exception as e:
        print(f"Error displaying the {choice}: {e}")

def display_location(page):
    """Displays the exact location of the given country."""
    file_path = rf"graphics\satellite\{page}_large_locator.gif"
    if not os.path.exists(file_path):
        print(f"Error: Could not find the location for the page '{page}'.")
        return

    try:
        with Image.open(file_path) as img:
            img.show()
    except Exception as e:
        print(f"Error displaying the location: {e}")
        
def search_country_details(c,k):
    """Allows the user to search for details about a specific country."""
    while True:
        country = c.strip()
        if country.lower() == 'back':
            return

        country = country.title()

        try:
            with open("countryList.txt", "r") as file:
                country_line = next((line for line in file if country in line), None)

            if not country_line:
                print("Country not found. Please try again.")
                continue

            name = country_line[:2].strip()
            with open(f"mobile/{name}.html", "r", encoding="utf-8") as file:
                html_content = file.read()
    
            while True:
                key = k.strip()
                if key.lower() == 'exit':
                    print("Exiting the script. Goodbye!")
                    return
                
                results = extract_data(key, html_content)
                m = []
                if results:
                    for k, v in results.items():
                        m.append(f"{k}: {v}")
                else:
                    m.append(f"No results found for '{key}'. Please try again.")
                return m
        except FileNotFoundError:
            print("Error: 'countryList.txt' file not found.")

def extract_data(key, html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all <dt> and <dd> tags (definitions and their values)
    dt_elements = soup.find_all('dt')
    dd_elements = soup.find_all('dd')
    
    # Create a dictionary mapping <dt> text to corresponding <dd> text
    data = {}
    for dt, dd in zip(dt_elements, dd_elements):
        key_text = dt.get_text(strip=True)
        value_text = dd.get_text(strip=True)
        data[key_text] = value_text
    
    # Search for the entered key in the dictionary
    results = {k: v for k, v in data.items() if key.lower() in k.lower()}
    
    return results


def seelocation():
    """Displays the exact location of a country."""
    while True:
        country = input("Enter a country (or type 'BACK' to return to the menu): ").strip()
        if country.lower() == 'back':
            return

        country = country.title()

        try:
            with open("countryList.txt", "r") as file:
                country_line = next((line for line in file if country in line), None)

            if not country_line:
                print("Country not found. Please try again.")
                continue

            page = country_line[:2].strip()
            display_location(page)

        except FileNotFoundError:
            print("Error: 'countryList.txt' file not found.")




def expert_system():
    """Runs the expert system for live, work, or travel suggestions."""
    try:
        country_details = load_country_details()
        ask_question(country_details)
    except FileNotFoundError:
        print("Error: Required data file 'countries.csv' not found.")

def load_country_details():
    """Loads country details from a CSV file."""
    country_details = {}

    with open("countries.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            country_details[row['Country'].strip().lower()] = {
                "type of government": row['Type of Government'].strip().lower(),
                "field domain": row['Field Domain'].strip().lower(),
                "major religion": row['Major Religion'].strip().lower(),
                "gdp": row['GDP'].strip().lower(),
                #"population density": row['Population Density'].strip(),
                "average weather": row['Average weather'].strip().lower(),
                "import": row['Import'].strip().lower(),
                "export": row['Export'].strip().lower(),
                "trade type": row['Trade type'].strip().lower()
            }

    return country_details

def ask_question(country_details):
    """Prompts the user with questions to decide their needs."""
    while True:
        print("\nChoose the type of suggestion you need:")
        print("\t1. Living suggestions.")
        print("\t2. Working suggestions.")
        print("\t3. Traveling suggestions.")
        print("\t4. Go back to the main menu.")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                live_suggestion(country_details)
            elif choice == 2:
                work_suggestion(country_details)
            elif choice == 3:
                tourism_suggestion()
            elif choice == 4:
                return
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def live_suggestion(w):
    """Provides suggestions for living based on user preferences."""
    country_details = load_country_details()

    # Gather user preferences, allowing empty inputs
    '''preferences = {
       # "population density": input("Do you prefer high or low population density? ").strip().lower(),
        "average weather": input("What kind of climate do you prefer (cold, moderate, hot)? ").strip().lower(),
        "type of government": input("What type of government do you prefer? ").strip().lower(),
        "major religion": input("What is your religion? ").strip().lower()
    }'''
    preferences = {
        "average weather": w.strip().lower(),
    }

    # Filter countries based on provided preferences
    matches = [
        country for country, details in country_details.items()
        if all(
            (key in details and preferences[key] in details[key])
            for key in preferences if preferences[key]
        )
    ]
    m = []
    # Display results
    if matches:
        m.append("Countries that match your preferences:")
        for match in matches:
            m.append(f"- {match.title()}\n")
    else:
        m.append("\nNo countries match your preferences.")
    return m

def work_suggestion(w):
    """Provides suggestions for working based on user preferences."""
    country_details = load_country_details()
    field = w.strip().lower()
    matches = [country for country, details in country_details.items()
               if field in details.get("field domain", "")]

    m = []
    if matches:
        m.append("Countries with opportunities in your field:")
        for match in matches:
            m.append(f"- {match.title()}")
    else:
        m.append("\nNo countries found with opportunities in your field.")
    return m

def tourism_suggestion(budget, place_type):
    """Suggests travel destinations based on budget and preferences."""
    try:
        with open("Tourism.csv", "r") as file:
            reader = csv.DictReader(file)
            destinations = [row for row in reader]

        budget = float(budget)
        place_type = place_type.lower()

        matches = [dest for dest in destinations
                   if float(dest['Budget']) == budget and dest['Type of place'].lower() == place_type]
        
        m = []
         # Display results
        if matches:
            m.append("Top places you can visit:")
            for match in matches:
                m.append(f"-{match['Name of place'].title()}, {match['Country'].title()}")
        else:
            m.append("No destinations match your preferences.")
        return m
    except FileNotFoundError:
        print("Error: 'Tourism.csv' file not found.")

if __name__ == "__main__":
    select()
