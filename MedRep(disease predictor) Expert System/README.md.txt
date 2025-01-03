MedRep_README

Overview
----------------------
MedRep is a simple disease prediction and treatment suggestion application developed using Python and the Tkinter library. This application helps users input their symptoms, predict possible diseases, and suggest appropriate treatments. It also provides links to more information about each disease.

Features
-----------------------
Disease Prediction
Users can enter their symptoms, and the app predicts possible diseases based on the symptoms.

Treatment Suggestions
For each predicted disease, the app provides a list of suggested treatments.

Interactive UI
A user-friendly graphical interface built using Tkinter.
Includes a scrollable textbox for entering symptoms and viewing results.

Symptom Suggestions
A listbox that displays common symptoms to assist users in symptom entry.

More Information
More Info buttons for each disease that link to additional resources on WebMD.



How to Run
--------------------------
Prerequisites
Python 3.7 or later.
Required Libraries: tkinter, Pillow, requests.

Install missing dependencies using pip install pillow requests.

Steps to Run
----------------------------
Save the code in a file named medrep.py.
Open a terminal or command prompt and navigate to the directory containing medrep.py.
Run the application using python medrep.py.

File Structure
-----------------------------
The application consists of the following main components:

Classes
Disease: Represents a disease with its name, symptoms, and treatments.
Treatment: Represents a treatment with its name and type.
Person: Represents the user with their name and entered symptoms.
DiseasePredictor: The main logic for predicting diseases and suggesting treatments.

Functions
submit_symptoms: Handles user input, processes symptoms, and displays results.
open_more_info: Opens a browser window with more information about a disease.
populate_symptom_list: Populates the listbox with suggested symptoms.
add_selected_symptom: Adds the selected symptom from the listbox to the symptom entry box.

Usage Instructions
--------------------------
Enter Your Name
Input your name in the provided text field.

Input Symptoms
Enter symptoms line by line in the scrollable text box. Press Enter after each symptom.

Submit Symptoms
Click the Done button to see the predicted diseases and treatments.

View Results
The results will be displayed in the results box.
Click on More Info for additional details about a specific disease.

Future Enhancements
----------------------------
Add support for multi-language interfaces.
Include more diseases and symptoms in the database.
Implement machine learning for improved prediction accuracy.
Integrate voice input for symptom entry.

Contributions
-----------------------------
Contributions are welcome. Feel free to fork this repository and submit pull requests for new features or bug fixes.