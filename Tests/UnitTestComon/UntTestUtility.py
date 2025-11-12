import csv
import json
import yaml

import os

def Nothing():
    ...

def almost_equal(a, b, tol=1e-6):
    return abs(a - b) < tol

def Generate_sequence(n):
    """Generate a simple increasing numeric sequence."""
    return [float(i + 1) for i in range(n)]

def write_csv_for_test(file_path, lines):
    """Helper function to write raw CSV lines for testing."""
    with open(file_path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def read_csv_test(file_path, delimiter=','):
    """Helper to read CSV back into list-of-dicts for testing."""
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        return list(reader)
    
def write_json_test(file_path, data):
    """Helper function to create JSON files for testing read_json."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def read_json_test(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def write_yaml_test(file_path, data):
    """Helper to write YAML files for testing read function."""
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)

def read_yaml_test(file_path):
    """Helper function to read YAML for test verification."""
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
    
def write_config_test(file_path, data):
    """Write a JSON or YAML file for testing."""
    ext = os.path.splitext(file_path)[1].lower()

    with open(file_path, "w", encoding="utf-8") as f:
        if ext == ".json":
            write_json_test(file_path, data)
        elif ext in [".yaml", ".yml"]:
            write_yaml_test(file_path, data)
        else:
            raise ValueError("Unsupported test config type")

# Sample test data
sample_data = [
    {"name": "Alice", "age": 30, "score": 95.5},
    {"name": "Bob", "age": 25, "score": 88.2},
]

# Complex test data
Complex_data = [
    {"greeting": "こんにちは", "key": "üñîçødë"},
]

New_data = [
    {"name": "Jacob", "age": 23, "score": 50.9},
    {"name": "Tory", "age": 21, "score": 99.8},
]

sample_config = {
    "university": {
        "name": "GTB University",
        "department": "Robotics Engineering"
    },
    "students": [
        {"id": 1, "name": "Alice", "project": "Autonomous Rover"},
        {"id": 2, "name": "Bob", "project": "Drone Swarm Control"}
    ],
    "projects": {
        "active": [
            {"title": "Autonomous Rover", "progress": 65, "supervisor": "Dr. Grey"},
            {"title": "Drone Swarm Control", "progress": 40, "supervisor": "Dr. Lin"}
        ],
        "completed": []
    },
    "lab_settings": {
        "open_hours": "08:00-18:00",
        "max_students": 10,
        "equipment": {
            "3D_printers": 2,
            "robots": ["Atlas", "Spot", "Rover"]
        }
    }
}