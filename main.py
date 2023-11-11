import csv
import os
import tkinter as tk
from tkinter import simpledialog

#reading into the file with r module and defininf rhe csv file module
def read_file(csv_file_location):
    with open(csv_file_location, "r") as file:
        example_file = csv.DictReader(file)
        example_list = list(example_file)
    return example_list

#parsing through data with a for loop to iterate field name
def process_data(example_list):
    field_data = {}
    for example_data in example_list:
        field_name = example_data.get("Field")
        if field_name:
            if field_name in field_data:
                field_data[field_name] += 1
            else:
                field_data[field_name] = 1
    return field_data

#write a report to the report.txt file to keep track of changes in a sorted dictionary
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k, v in sorted(dictionary.items()):
            f.write(f"{k}: {v}\n")

#Set up a GUI using the tkinter module
def get_user_input():
    root = tk.Tk()
    root.withdraw()
    field_to_check = simpledialog.askstring("Input", "Enter Field to Check:")
    value_to_check = simpledialog.askstring("Input", "Enter Value to Check:")
    return field_to_check, value_to_check

#again will itterate through the list in the csv file going through Field and Value seeing if they exist

def is_field_value_pair_exist(example_list, field, value):
    for example_data in example_list:
        example_field = example_data.get("Field")
        example_value = example_data.get("Value")
        if example_field is not None:
            example_field = example_field.strip()
        if example_value is not None:
            example_value = example_value.strip()

        if example_field == field and example_value == value:
            return True

    return False

#declaring awhere the supporting files are located in your local computer

csv_file_path = "C:\\PyPractice\\CSV_Reader\\ExScript\\ExFile.csv"
report_file_path = "C:\\PyPractice\\CSV_Reader\\ExScript\\Report.txt"
example_list = read_file(csv_file_path)
dictionary = process_data(example_list)
write_report(dictionary, report_file_path)

#statements found for executables in the script
print("Data Loading Status...")
if os.path.isfile(report_file_path):
    print("Successfully Loaded!")
else:
    print("Data has not loaded!")

#info fed into GUI 

field_to_check, value_to_check = get_user_input()

print("Loaded entries:", example_list)

print(f"Checking if the field-value pair ({field_to_check}, {value_to_check}) exists...")

#will loop through list again to see if there are any aditional entries 
for example_data in example_list:
    print(f"Entry in CSV: {example_data}")

if is_field_value_pair_exist(example_list, field_to_check, value_to_check):
    print(f"The field-value pair ({field_to_check}, {value_to_check}) exists.")
else:
    print(f"The field-value pair ({field_to_check}, {value_to_check}) does not exist.")


