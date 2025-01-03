import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
import requests
from io import BytesIO
import webbrowser

class Disease:
    def __init__(self, name, symptoms, treatments):
        self.name = name
        self.symptoms = [symptom.lower() for symptom in symptoms]
        self.treatments = treatments

class Treatment:
    def __init__(self, name, type_of_treatment):
        self.name = name
        self.type_of_treatment = type_of_treatment

class Person:
    def __init__(self, name):
        self.name = name
        self.symptoms = []

    def add_symptom(self, symptom):
        self.symptoms.append(symptom.lower())

class DiseasePredictor:
    def __init__(self, diseases):
        self.diseases = diseases

    def predict_disease(self, person):
        possible_diseases = []
        for disease in self.diseases.values():
            matching_symptoms = [symptom for symptom in disease.symptoms if symptom in person.symptoms]
            if matching_symptoms:
                possible_diseases.append(disease)
        return possible_diseases

    def suggest_treatment(self, disease_name):
        for disease in self.diseases.values():
            if disease.name.lower() == disease_name.lower():
                return [treatment.name for treatment in disease.treatments]
        return "Treatment not available"

diseases = {
    "heart_disease": Disease(
        "Heart Disease", 
        ["chest_pain", "shortness_of_breath"],
        [
            Treatment("Nitroglycerin", "Medication"), 
            Treatment("Lifestyle changes", "General care")
        ]
    ),
    "common_cold": Disease(
        "Common Cold", 
        ["runny_nose", "sore_throat", "cough", "sneezing", "headache", "fever", "fatigue"],
        [
            Treatment("Rest", "General care"), 
            Treatment("Hydration", "Symptom relief")
        ]
    ),
    "covid-19": Disease(
        "COVID-19", 
        ["fever", "cough", "loss of taste or smell"],
        [
            Treatment("Isolation", "Prevention"), 
            Treatment("Antiviral medication", "Medication")
        ]
    ),
    "cold": Disease(
        "Cold", 
        ["runny nose", "sneezing", "cough"],
        [
            Treatment("Decongestant", "Symptom relief"), 
            Treatment("Rest", "General care")
        ]
    ),
    "hay_fever": Disease(
        "Hay Fever", 
        ["sneezing", "itchy_eyes", "runny_nose", "nasal_congestion", "fatigue"],
        [
            Treatment("Antihistamines", "Medication"), 
            Treatment("Decongestants", "Symptom relief")
        ]
    ),
    "food_allergy": Disease(
        "Food Allergy", 
        ["tingling_mouth", "swelling_lips_tongue", "nausea", "diarrhea", "vomiting"],
        [
            Treatment("Avoid allergenic foods", "Prevention"), 
            Treatment("Epinephrine auto-injector", "Emergency care")
        ]
    ),
    "insect_sting_allergy": Disease(
        "Insect Sting Allergy", 
        ["pain_sting_site", "large_edema", "rapid_heartbeat", "shortness_of_breath", "flushing"],
        [
            Treatment("Cold compress", "Symptom relief"), 
            Treatment("Antihistamines", "Medication"),
            Treatment("Epinephrine auto-injector", "Emergency care")
        ]
    ),
    "medicine_allergy": Disease(
        "Medicine Allergy", 
        ["rash", "itching", "swelling_face", "dizziness", "fever"],
        [
            Treatment("Stop medication", "General care"), 
            Treatment("Antihistamines", "Medication"),
            Treatment("Consult a doctor", "Emergency care")
        ]
    ),
    "atopic_dermatitis": Disease(
        "Atopic Dermatitis", 
        ["red_patches", "scaling_skin", "cracked_skin", "peeling_skin"],
        [
            Treatment("Moisturizer", "Symptom relief"), 
            Treatment("Topical corticosteroids", "Medication"),
            Treatment("Avoid triggers", "Prevention")
        ]
    ),
    "dust_mite_allergy": Disease(
        "Dust Mite Allergy", 
        ["postnasal_drip", "itchy_throat", "stuffy_nose", "coughing", "watery_eyes"],
        [
            Treatment("Allergen-proof covers", "Prevention"), 
            Treatment("Regular cleaning", "General care"),
            Treatment("Antihistamines", "Medication")
        ]
    ),
    "ischemic_stroke": Disease(
        "Ischemic Stroke", 
        ["weakness on one side", "difficulty speaking", "vision loss", "dizziness"],
        [
            Treatment("Clot-busting drugs (tPA)", "Emergency care"), 
            Treatment("Antiplatelet medications", "Medication"),
            Treatment("Clot removal surgery", "Intervention")
        ]
    ),
    "hemorrhagic_stroke": Disease(
        "Hemorrhagic Stroke", 
        ["Severe and sudden headache", "loss of consciousness", "vomiting", "confusion"],
        [
            Treatment("Control bleeding", "Medication"), 
            Treatment("Stop blood thinners", "General care"),
            Treatment("Surgery", "Intervention")
        ]
    ),
    "type_1_diabetes": Disease(
        "Type 1 Diabetes", 
        ["excessive thirst", "frequent urination", "extreme hunger"],
        [
            Treatment("Insulin therapy", "Medication")
        ]
    ),
    "type_2_diabetes": Disease(
        "Type 2 Diabetes", 
        ["blurred vision", "slow-healing wounds", "fatigue"],
        [
            Treatment("Lifestyle changes", "Prevention"), 
            Treatment("Oral medications", "Medication")
        ]
    ),
    "gestational_diabetes": Disease(
        "Gestational Diabetes", 
        ["excessive thirst", "frequent urination", "fatigue"],
        [
            Treatment("Blood sugar monitoring", "General care"), 
            Treatment("Healthy diet", "Prevention")
        ]
    ),
    "mold_allergy": Disease(
        "Mold Allergy", 
        ["chest_tightness", "breathing_difficulty", "skin_irritation", "night_cough", "headache"],
        [
            Treatment("Reduce humidity", "Prevention"), 
            Treatment("Antihistamines", "Medication")
        ]
    ),
    "animal_dander_allergy": Disease(
        "Animal Dander Allergy", 
        ["skin_rash", "scratchy_throat", "runny_eyes", "sneezing"],
        [
            Treatment("Avoid animals", "Prevention"), 
            Treatment("Air purifiers", "General care"),
            Treatment("Antihistamines", "Medication")
        ]
    ),
    "latex_allergy": Disease(
        "Latex Allergy", 
        ["hives", "swelling_hands", "chest_pain", "blisters", "burning_skin"],
        [
            Treatment("Avoid latex products", "Prevention"), 
            Treatment("Antihistamines", "Medication"),
            Treatment("Epinephrine auto-injector", "Emergency care")
        ]
    )
}

def create_gui():
    def submit_symptoms():
        name = name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return
            
        person = Person(name)
        symptoms = symptom_entry.get("1.0", tk.END).strip().splitlines()
        
        for symptom in symptoms:
            if symptom.lower() != 'done' and symptom:
                person.add_symptom(symptom.lower())
        
        predicted_diseases = predictor.predict_disease(person)
        
        result_box.config(state=tk.NORMAL)
        result_box.delete("1.0", tk.END)
        
        if predicted_diseases:
            header_text = f"Possible disease(s) for {person.name} based on symptoms:\n"
            result_box.insert(tk.END, header_text, "header")
            
            for disease in predicted_diseases:
                result_box.insert(tk.END, f"- {disease.name}\n", "disease")
                result_box.insert(tk.END, "  Suggested treatment(s):\n", "default")
                treatments = predictor.suggest_treatment(disease.name)
                for treatment in treatments:
                    result_box.insert(tk.END, "    * ", "default")
                    result_box.insert(tk.END, treatment, "emoji_text")
                    result_box.insert(tk.END, " 💊\n", "emoji")
                
                more_info_button = tk.Button(result_box, text="More Info", bg="Sky Blue", fg="white", font=("Arial", 10),
                                             command=lambda d=disease.name: open_more_info(d))
                result_box.window_create(tk.END, window=more_info_button)
                result_box.insert(tk.END, "\n\n")
        else:
            no_disease_text = f"No disease predicted for {person.name} based on provided symptoms."
            result_box.insert(tk.END, no_disease_text, "header")
        
        result_box.config(state=tk.DISABLED)
    
    def open_more_info(disease_name):
        if disease_name:
            formatted_disease_name = disease_name.replace("_", " ").replace("  ", " ")
            webbrowser.open(f"https://www.webmd.com/search/search_results/default.aspx?query={formatted_disease_name}")
    
    def populate_symptom_list():
        unique_symptoms = set()
        for disease in diseases.values():
            unique_symptoms.update(disease.symptoms)
        
        for symptom in sorted(unique_symptoms):
            symptom_listbox.insert(tk.END, symptom)

    def add_selected_symptom(event):
        selected = symptom_listbox.curselection()
        if selected:
            symptom = symptom_listbox.get(selected[0])
            symptom_entry.insert(tk.END, f"{symptom}\n")
    
    root = tk.Tk()
    root.title("MedRep")
    root.geometry("900x1100")  

    url = "https://www.thearabhospital.com/wp-content/uploads/2021/05/%D8%A7%D9%84%D8%B7%D8%A8%D9%8A-%D8%A7%D9%84%D8%A7%D9%95%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A-%D9%88%D8%A7%D9%84%D8%B3%D9%91%D8%AC%D9%84-%D8%A7%D9%84%D8%B5%D8%AD%D9%8A-%D8%A7%D9%84%D8%A7%D9%95%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A.jpg"
    try:
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        img_data = img_data.resize((900, 1100), Image.LANCZOS)
        img = ImageTk.PhotoImage(img_data)
    
        background_label = tk.Label(root, image=img)
        background_label.place(relx=0.5, rely=0, relwidth=0.8, relheight=1)
    except Exception as e:
        messagebox.showerror("Image Load Error", f"Failed to load background image.\n{e}")

    system_name = tk.Label(root, text="MedRep", font=("Arial", 24, "bold"), fg="Deep Sky Blue", bg="#f0f0f0")
    system_name.place(relx=0.25, y=1)

    input_frame = tk.Frame(root, bg="#f0f0f0", bd=5)
    input_frame.place(relx=0.0, rely=0.05, relwidth=0.4, relheight=0.3)

    tk.Label(input_frame, text="Enter Your Name:-", fg="Deep Sky Blue", bg="#f0f0f0", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=7)
    name_entry = tk.Entry(input_frame, font=("Arial", 12), fg="gray", width=25)
    name_entry.pack(padx=10, pady=5)

    tk.Label(input_frame, text="Enter Symptoms (line by line):", fg="Deep Sky Blue", bg="#f0f0f0", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)
    symptom_entry = scrolledtext.ScrolledText(input_frame, height=5, font=("Arial", 12), fg="gray")
    symptom_entry.pack(padx=10, pady=5)

    symptom_list_frame = tk.Frame(root, bg="#f0f0f0", bd=5)
    symptom_list_frame.place(relx=0.0, rely=0.35, relwidth=0.3, relheight=0.25)

    tk.Label(symptom_list_frame, text="Some suggested symptoms to help you:-", fg="Deep Sky Blue", bg="#f0f0f0", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=5)
    symptom_listbox = tk.Listbox(symptom_list_frame, height=10, font=("Arial", 12), fg="gray", selectmode=tk.SINGLE)
    symptom_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    populate_symptom_list()

    symptom_listbox.bind("<ButtonRelease-1>", add_selected_symptom)

    button_frame = tk.Frame(root, bg="#f0f0f0", bd=5)
    button_frame.place(relx=0.3, rely=0.35, relwidth=0.1, relheight=0.25)

    submit_button = tk.Button(button_frame, text="Done", command=submit_symptoms, bg="Sky Blue", fg="white", font=("Arial", 18))
    submit_button.pack(expand=True, pady=5)

    result_frame = tk.Frame(root, bg="#f0f0f0", bd=5)
    result_frame.place(relx=0.0, rely=0.65, relwidth=0.4, relheight=0.3)

    tk.Label(result_frame, text="Results:-", fg="Deep Sky Blue", bg="#f0f0f0", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=5)
    result_box = scrolledtext.ScrolledText(result_frame, height=10, font=("Arial", 12), fg="gray")
    result_box.pack(padx=5, pady=5)
    result_box.config(state=tk.DISABLED)

    result_box.tag_configure("header", foreground="#004d73", font=("Arial", 14, "bold"))
    result_box.tag_configure("disease", foreground="#8d5100", font=("Arial", 12, "bold"))
    result_box.tag_configure("emoji", foreground="#8d2e00", font=("Arial", 12))
    result_box.tag_configure("emoji_text", foreground="#006fa6", font=("Arial", 12, "italic"))
    result_box.tag_configure("default", foreground="#003c5a", font=("Arial", 12))

    root.mainloop()

if __name__ == "__main__":
    predictor = DiseasePredictor(diseases)
    create_gui()