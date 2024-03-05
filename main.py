# main.py
import tkinter as tk
from database import fetch_person_data, add_person_data

def fetch_person(person_id=None):
    if person_id is not None:
        try:
            person_id = int(person_id)
            person_data = fetch_person_data(person_id)
            if person_data:
                name, hight, weight = person_data
                bmi = round(weight / ((hight / 100) ** 2), 2)
                bmi_text.set(f"Name: {name}\nHight: {hight} cm\nWeight: {weight} kg\nBMI: {bmi}")

                # Display recommendations based on BMI
                if bmi <= 18.5:
                    recommendation = "You are below the standard body mass; consider eating regularly and including fats in your diet."
                elif 18.5 <= bmi <= 24.9:
                    recommendation = "You have a normal standard weight."
                elif 25 <= bmi <= 29.9:
                    recommendation = "You are overweight; consider managing your weight."
                else:
                    recommendation = "You have obesity and need prompt medical attention."

                bmi_text.set(f"{bmi_text.get()}\n\nRecommendation: {recommendation}")

            else:
                bmi_text.set("No data found for selected person.")
        except ValueError:
            bmi_text.set("Invalid input for person ID.")
    else:
        bmi_text.set("No person ID provided.")


        
def add_new_person():
    name = name_entry.get()
    hight = int(hight_entry.get())
    weight = int(weight_entry.get())
    person_id = add_person_data(name, hight, weight)
    if isinstance(person_id, int):
        fetch_person(person_id)  # Pass the person_id to fetch_person


root = tk.Tk()
root.title("BMI Calculator")

# Create entry fields for new person's data
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

hight_label = tk.Label(root, text="Hight (cm):")
hight_label.grid(row=1, column=0, padx=5, pady=5)
hight_entry = tk.Entry(root)
hight_entry.grid(row=1, column=1, padx=5, pady=5)

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=2, column=0, padx=5, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=2, column=1, padx=5, pady=5)

person_id_label = tk.Label(root, text="Person ID:")
person_id_label.grid(row=3, column=0, padx=5, pady=5)
person_id_entry = tk.Entry(root)
person_id_entry.grid(row=3, column=1, padx=5, pady=5)

# Create buttons to fetch existing person's data and add new person's data
fetch_button = tk.Button(root, text="Fetch Person Data", command=lambda: fetch_person(person_id_entry.get()))

fetch_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

new_person_button = tk.Button(root, text="Add New Person Data", command=add_new_person)
new_person_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Create a text box to display BMI
bmi_text = tk.StringVar()
bmi_text.set("Select a person to display BMI.")
bmi_label = tk.Label(root, textvariable=bmi_text)
bmi_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
