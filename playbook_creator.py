import json
import os
import re
import math

def load_playbooks(file_path="playbooks/playbooks.json"):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: playbooks.json file not found.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format.\n{e}")
        return {}

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name.lower()) + ".yml"

def display_menu(playbooks):
    keys = list(playbooks.keys())
    total = len(keys)
    midpoint = math.ceil(total / 2)

    col1 = keys[:midpoint]
    col2 = keys[midpoint:]

    print("\nAvailable Ansible Playbook Templates:\n")
    for i in range(midpoint):
        left = f"{i+1:>2}. {col1[i]:<35}"
        right = f"{i+1+midpoint:>2}. {col2[i]:<35}" if i < len(col2) else ""
        print(f"{left} {right}")

def main():
    playbooks = load_playbooks()
    if not playbooks:
        return

    display_menu(playbooks)

    try:
        choice = int(input("\nEnter the number of the playbook you want to generate: "))
        keys = list(playbooks.keys())
        if choice < 1 or choice > len(keys):
            raise ValueError
        key = keys[choice - 1]
        content = playbooks[key]
        filename = sanitize_filename(key)
        with open(filename, "w") as f:
            f.write(content)
        print(f"\nPlaybook '{filename}' has been created successfully.")
    except ValueError:
        print("\nInvalid selection. Please enter a valid number.")
    except Exception as e:
        print(f"\nUnexpected error: {e}")

if __name__ == "__main__":
    main()
