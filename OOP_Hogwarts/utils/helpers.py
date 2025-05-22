# helper function (load/save, formatting, etc.) 

# Utility File

import json

def load_students():
    try:
        with open("data/students.json", "r") as file:
            return json.load(file)
    except:
        return []

def save_students(data):
    with open("data/students.json", "w") as file:
        json.dump(data, file, indent=4)
