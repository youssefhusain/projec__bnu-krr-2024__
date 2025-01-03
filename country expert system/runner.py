from tkinter import Tk, Label, Button, Entry, Toplevel, Scrollbar, Label, Scrollbar, Text, RIGHT, Y, END
import cmain
from PIL import Image, ImageTk

def go_to_choices():
    # Change background to the next image
    new_bg_image = Image.open("background2.png")  # Replace with your next background image
    new_bg_photo = ImageTk.PhotoImage(new_bg_image)
    bg_label.config(image=new_bg_photo)
    bg_label.image = new_bg_photo  # Keep a reference to the image

    # Remove the "Begin" button
    begin_button.place_forget()  # Use place_forget to remove the button
    for widget in root.winfo_children():
        if isinstance(widget, Button):
            widget.place_forget()
            
    # Add the choice buttons
    choice_button1 = Button(root, text="List the countries", font=("Arial", 14), fg="black",bg="brown", command=list_countries)
    choice_button1.pack(pady=10)
    choice_button1.place(x=240, y=320)  
    
    choice_button2 = Button(root, text="Country's details", font=("Arial", 14), fg="black",bg="brown", command=search)
    choice_button2.pack(pady=10)
    choice_button2.place(x=240, y=360)  
    
    choice_button3 = Button(root, text="Flag or map", font=("Arial", 14), fg="black",bg="brown", command=map_or_flag)
    choice_button3.pack(pady=10)
    choice_button3.place(x=240, y=400)  

    choice_button4 = Button(root, text="Location", font=("Arial", 14), fg="black",bg="brown", command=location)
    choice_button4.pack(pady=10)
    choice_button4.place(x=460, y=320)  

    choice_button5 = Button(root, text="Expert system", font=("Arial", 14), fg="black",bg="brown", command=open_expert_system)
    choice_button5.pack(pady=10)
    choice_button5.place(x=460, y=360)  

    choice_button6 = Button(root, text="Exit", font=("Arial", 14), fg="black",bg="brown", command=root.destroy)
    choice_button6.pack(pady=10)
    choice_button6.place(x=460, y=400)
    
def location():
    # Change background when entering the country input screen
    new_bg_image = Image.open("background3.png")  # Replace with your desired background image after choosing 4
    new_bg_photo = ImageTk.PhotoImage(new_bg_image)
    bg_label.config(image=new_bg_photo)
    bg_label.image = new_bg_photo  # Keep a reference to the image

    # Remove the choice buttons
    for widget in root.winfo_children():
        if isinstance(widget, Button):
            widget.place_forget()

    # Add the country input label
    country_label = Label(root, text="Enter the country name:", font=("Arial", 14))
    country_label.place(x=290, y=135)

    # Add the country input box
    country_entry = Entry(root, font=("Arial", 14))
    country_entry.place(x=280, y=175)

    # Add the submit button
    submit_button = Button(root, text="Submit", font=("Arial", 14), bg="brown", fg="black",command=lambda: loc(country_entry.get()))
    submit_button.place(x=350, y=215)

    # Add the back button
    back_button = Button(root, text="Back", font=("Arial", 14), fg="black",bg="brown", command=remove)
    back_button.place(x=357, y=265)
    
def search():
    """Ask the user for a country and a keyword to search and return the results."""
    # Remove previous widgets and change the background
    for widget in root.winfo_children():
        if widget != bg_label:  # Keep the background image
            widget.place_forget()

    # Set up the background image
    new_bg_image = Image.open("background3.png")  
    new_bg_photo = ImageTk.PhotoImage(new_bg_image)
    bg_label.config(image=new_bg_photo)
    bg_label.image = new_bg_photo  # Keep a reference to the image

    # Add the input label and entry field for country
    country_label = Label(root, text="country name", font=("Arial", 14))
    country_label.place(x=325, y=150)

    country_entry = Entry(root, font=("Arial", 14))
    country_entry.place(x=270, y=190)

    # Add the input label and entry field for keyword
    keyword_label = Label(root, text="keyword", font=("Arial", 14))
    keyword_label.place(x=340, y=230)

    keyword_entry = Entry(root, font=("Arial", 14))
    keyword_entry.place(x=270, y=270)

    # Add a submit button that will call the search function
    submit_button = Button(root, text="Submit", font=("Arial", 14), bg="brown", command=lambda:rib(country_entry.get(), keyword_entry.get()))
    submit_button.place(x=340, y=310)

    # Add a back button to go back to the main choices screen
    back_button = Button(root, text="Back", font=("Arial", 14), bg="brown", command=remove)
    back_button.place(x=348, y=350)
    
def map_or_flag():
    """Switch to map or flag selection screen."""
    # Change background when entering the map/flag selection screen
    new_bg_image = Image.open("background3.png")  
    new_bg_photo = ImageTk.PhotoImage(new_bg_image)
    bg_label.config(image=new_bg_photo)
    bg_label.image = new_bg_photo  # Keep a reference to the image

    # Remove all other widgets
    for widget in root.winfo_children():
        if isinstance(widget, Button):
            widget.place_forget()

    country_label = Label(root, text="Enter the country name:", font=("Arial", 14))
    country_label.place(x=290, y=135)

    # Add the country input box
    country_entry = Entry(root, font=("Arial", 14))
    country_entry.place(x=280, y=175)

    # Add buttons for map or flag selection
    map_button = Button(root, text="Map", font=("Arial", 14), bg="brown", command=lambda: send("map", country_entry.get()))
    map_button.place(x=310, y=215)

    flag_button = Button(root, text="Flag", font=("Arial", 14), bg="brown", command=lambda:send("flag", country_entry.get()))
    flag_button.place(x=410, y=215)

    # Add back button
    back_button = Button(root, text="Back", font=("Arial", 14), bg="brown", command=remove)
    back_button.place(x=357, y=270)

def list_countries():
    # Change background when showing the list of countries
    list_window = Toplevel(root)
    list_window.title("List of Countries")
    list_window.geometry("600x400")
    
    # Add a scrollable text box
    scroll_bar = Scrollbar(list_window)
    scroll_bar.pack(side="right", fill="y")
    
    text_widget = Text(list_window, wrap="word", font=("Arial", 12), yscrollcommand=scroll_bar.set)
    text_widget.pack(expand=True, fill="both")
    scroll_bar.config(command=text_widget.yview)

    # Load and display countries
    try:
        with open("countryList.txt", "r") as file:
            countries = file.readlines()
            text_widget.insert("1.0", "".join(countries))  # Add country list to the text widget
            text_widget.config(state="disabled")  # Make read-only
    except FileNotFoundError:
        text_widget.insert("1.0", "Error: 'countries.txt' file not found.")
        text_widget.config(state="disabled")

    # Add a "Close" button
    close_button = Button(list_window, text="Close", font=("Arial", 14), bg="brown", command=list_window.destroy)
    close_button.pack(pady=10)


def open_expert_system():
    """Open the expert system with four options in the same window."""
    # Remove all widgets except the background label
    for widget in root.winfo_children():
        if widget != bg_label:
            widget.place_forget()

    # Change the background or keep it
    new_bg_image = Image.open("background3.png")  
    new_bg_photo = ImageTk.PhotoImage(new_bg_image)
    bg_label.config(image=new_bg_photo)
    bg_label.image = new_bg_photo  # Keep a reference to the image

    # Add four buttons
    living_button = Button(root, text="Living Suggestions      ", font=("Arial", 14), bg="brown", command=living_suggestions)
    living_button.place(x=270, y=230)

    working_button = Button(root, text="Working Suggestions  ", font=("Arial", 14), bg="brown", command=working_suggestions)
    working_button.place(x=270, y=270)

    traveling_button = Button(root, text="Traveling Suggestions", font=("Arial", 14), bg="brown", command=tourism_suggestions)
    traveling_button.place(x=270, y=310)

    back_button = Button(root, text="Back", font=("Arial", 14), bg="brown", command=go_to_choices)
    back_button.place(x=340, y=350)

def living_suggestions():
    """Open a new page to ask for weather preference."""
    # Remove previous buttons and change background
    for widget in root.winfo_children():
        if widget != bg_label:  # Keep the background image
            widget.place_forget()

    # Change the background or keep it
    new_bg_image = Image.open("background3.png")  
    new_bg_photo = ImageTk.PhotoImage(new_bg_image)
    bg_label.config(image=new_bg_photo)
    bg_label.image = new_bg_photo  # Keep a reference to the image

    # Add label and entry for weather preference
    weather_label = Label(root, text="Enter desired weather cold, moderate, hot:", font=("Arial", 14))
    weather_label.place(x=200, y=150)

    weather_entry = Entry(root, font=("Arial", 14))
    weather_entry.place(x=260, y=190)

    submit_button = Button(root, text="Submit", font=("Arial", 14), bg="brown", command=lambda: live(weather_entry.get()))
    submit_button.place(x=330, y=230)

    back_button = Button(root, text="Back", font=("Arial", 14), bg="brown", command=open_expert_system)
    back_button.place(x=337, y=270)

def working_suggestions():
    """Open a new page to ask for work-related preference."""
    # Remove previous buttons and change background
    for widget in root.winfo_children():
        if widget != bg_label:  # Keep the background image
            widget.place_forget()

    # Change the background or keep it
    new_bg_image = Image.open("background3.png") 
    new_bg_photo = ImageTk.PhotoImage(new_bg_image)
    bg_label.config(image=new_bg_photo)
    bg_label.image = new_bg_photo  # Keep a reference to the image

    # Add label and entry for work preference (similar to weather preference)
    work_label = Label(root, text="Enter your desired work environment (e.g., technology, manufacturing, tourism):", font=("Arial", 14))
    work_label.place(x=40, y=150)

    work_entry = Entry(root, font=("Arial", 14))
    work_entry.place(x=260, y=190)

    submit_button = Button(root, text="Submit", font=("Arial", 14), bg="brown", command=lambda: work(work_entry.get()))
    submit_button.place(x=330, y=230)

    back_button = Button(root, text="Back", font=("Arial", 14), bg="brown", command=open_expert_system)
    back_button.place(x=337, y=270)

def tourism_suggestions():
    """Open a new page to ask for tourism-related preferences."""
    # Remove previous buttons and change background
    for widget in root.winfo_children():
        if widget != bg_label:  
            widget.place_forget()

    # Change the background or keep it
    new_bg_image = Image.open("background3.png")  
    new_bg_photo = ImageTk.PhotoImage(new_bg_image)
    bg_label.config(image=new_bg_photo)
    bg_label.image = new_bg_photo  # Keep a reference to the image

    # Create labels and input fields for budget and type of destination
    budget_label = Label(root, text="Enter your budget (e.g., 1, 2, 2.5)10K:", font=("Arial", 14))
    budget_label.place(x=180, y=150)

    budget_entry = Entry(root, font=("Arial", 14))
    budget_entry.place(x=240, y=190)

    destination_label = Label(root, text="Enter destination type (e.g., historical, adventure, beach):", font=("Arial", 14))
    destination_label.place(x=100, y=230)

    destination_entry = Entry(root, font=("Arial", 14))
    destination_entry.place(x=240, y=270)

    submit_button = Button(root, text="Submit", font=("Arial", 14), bg="brown", command=lambda: tourism(budget_entry.get(), destination_entry.get()))
    submit_button.place(x=315, y=310)

    back_button = Button(root, text="Back", font=("Arial", 14), bg="brown", command=open_expert_system)
    back_button.place(x=322, y=350)

def remove():
    """Removes the label and entry widgets for country input."""
    for widget in root.winfo_children():
        if isinstance(widget, Label) and (widget.cget("text") == "Enter the country name:" or widget.cget("text") == "country name" or widget.cget("text") == "keyword"):
            widget.destroy()  # Remove the specific label
        if isinstance(widget, Entry):
            widget.destroy()  
        
    go_to_choices()
    
def send(choice, country):
    """Send the user's choice and country to the main program."""
    country = country.title().strip()

    try:
        with open("countryList.txt", "r") as file:
            country_line = next((line for line in file if country in line), None)
        
        if not country_line:
            print("Country not found. Please try again.")
            return

        page = country_line[:2].strip()
        cmain.display_map_or_flag(page, choice)
    
    except FileNotFoundError:
        print("Error: 'countryList.txt' file not found.")
        return
    
def loc(country):
    """Send the country to the main program to get the location."""
    country = country.title().strip()
    try:
        with open("countryList.txt", "r") as file:
            country_line = next((line for line in file if country in line), None)
        
        if not country_line:
            print("Country not found. Please try again.")
            return

        page = country_line[:2].strip()
        cmain.display_location(page)
    
    except FileNotFoundError:
        print("Error: 'countryList.txt' file not found.")
        return    
    
def live(weather):
    m = cmain.live_suggestion(weather)
    window(m)
def work(work):
   
    m = cmain.work_suggestion(work)
    window(m)
    
def tourism(budget, destination):
    m = cmain.tourism_suggestion(budget, destination)
    window(m)   
    
def rib(country, keyword):
    m = cmain.search_country_details(country, keyword)
    window(m)
        
        
def window(content):
    """Open a new window and display the provided multiline string."""
    # Create a new window
    result_window = Toplevel()
    result_window.title("Tourism Suggestions")
    result_window.geometry("400x400")
    
    # Add a scrollbar
    scrollbar = Scrollbar(result_window)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    # Create a Text widget to display multiline content
    text_widget = Text(result_window, wrap="word", yscrollcommand=scrollbar.set, font=("Arial", 12))
    text_widget.pack(expand=True, fill="both", padx=10, pady=10)
    
    # Insert the multiline content
    text_widget.insert(END, "\n".join(content))
    text_widget.config(state="disabled")  # Make it read-only
    
    # Configure the scrollbar
    scrollbar.config(command=text_widget.yview)

    

# Main window setup
root = Tk()
root.title("Georgical Project")
root.geometry("800x600")

# Set initial background image
bg_image = Image.open("background.png")  # Replace with your initial image file
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Add the "Begin" button
begin_button = Button(root, text="Start", font=("Arial", 20), command=go_to_choices, bg="brown", fg="black")
begin_button.place(x=250, y=310)  # Place button at (250, 310)

# Run the main window
root.mainloop()
