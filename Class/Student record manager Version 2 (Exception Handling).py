"""Student Record Management System (beginner console project).

Concepts demonstrated: functions, lists/dictionaries, file handling,
JSON, loops, input validation, and exception handling.
"""


import json
import pandas
import streamlit as st

def load_records():
    """Return saved records. Start with an empty list if the file is new."""
    try:
        # pathlib version: with FILE_PATHS["records"].open("r", encoding="utf-8") as file:
        with open(r"C:\Users\bhava\Desktop\DA Course Material Day-Wise\Python\student_record_management\Class\student_data.json", "r", encoding="utf-8") as file: #replace FILE_PATHS["records"] with student_records.json
            records = json.load(file)

        if not isinstance(records, list):
            raise ValueError("The records file should contain a list.")
        required_fields = {"roll_number", "name", "course", "mark"}
        if any(not isinstance(record, dict) or not required_fields <= record.keys() for record in records):
            raise ValueError("One or more records have missing fields.")

        return records

    except FileNotFoundError:
        print("No records file found. Starting with an empty record list.")
        return []
    except json.JSONDecodeError:
        print("The records file is not valid JSON. Starting with an empty record list.")
        return []
    except ValueError as error:
        print(f"The records file has an invalid structure: {error}")
        return []


def save_records(records):
    """Save all records. Returns True only when saving succeeds."""
    try:
        # pathlib version: with FILE_PATHS["records"].open("w", encoding="utf-8") as file:
        with open(r"C:\Users\bhava\Desktop\DA Course Material Day-Wise\Python\student_record_management\Class\student_data.json", "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)
        return True
    except PermissionError:
        print("Permission denied. Records were not saved.")
    except TypeError as error:
        print(f"Cannot convert a record to JSON: {error}")
    except OSError as error:
        print(f"Could not save records: {error}")
    return False


def get_non_empty_input(message):
    """Keep asking until the user enters non-blank text."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This value cannot be empty.")


def get_mark():
    """Return a whole-number mark from 0 to 100."""
    while True:
        try:
            mark = int(input("Mark (0-100): ").strip())
            if 0 <= mark <= 100:
                return mark
            print("Enter a mark from 0 to 100.")
        except ValueError:
            print("Invalid mark. Enter a whole number, for example 78.")


def find_record(records, roll_number):
    """Return the matching record dictionary, or None when not found."""
    for record in records:
        if record["roll_number"] == roll_number:
            return record
    return None


def add_record(records):
    print("\n--- Add student ---")

    if find_record(records, roll_number):
        print("A student with that roll number already exists.")
        return

    record = {
        "roll_number": get_non_empty_input("Roll number: "),
        "name": get_non_empty_input("Name: ").title(),
        "course": get_non_empty_input("Course: ").title(),
        "mark": get_mark(),
    }
    records.append(record)

    if save_records(records):
        print("Student record added and saved.")


def view_records(records):

    print("\n --- View All Student Records ---")
    if not records:
        print("No student records available.")
        return

    try:
        df = pd.DataFrame(records)
        print(df)
    except ValueError as e:
        print(e)
        print("check data!")

    return "View record executed."


def search_record(records):
    print("\n--- Search student ---")
    roll_number = get_non_empty_input("Roll number: ")
    record = find_record(records, roll_number)

    if record:
        print(f"Name   : {record['name']}")
        print(f"Course : {record['course']}")
        print(f"Mark   : {record['mark']}")
    else:
        print("Student record not found.")


def update_mark(records):
    print("\n--- Update mark ---")
    roll_number = get_non_empty_input("Roll number: ")
    record = find_record(records, roll_number)

    if not record:
        print("Student record not found.")
        return

    record["mark"] = get_mark()
    if save_records(records):
        print("Mark updated and saved.")


def show_menu():
    print("\nSTUDENT RECORD MANAGEMENT")
    print("1. Add student")
    print("2. View all students")
    print("3. Search by roll number")
    print("4. Update mark")
    print("5. Create backup")
    print("6. Exit")


def main():
    records = load_records()

    actions = {
        "1": add_record,
        "2": view_records,
        "3": search_record,
        "4": update_mark
    }

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "5":
            # pathlib version: print(f"Goodbye. Your saved records remain in {FILE_PATHS['records'].name}.")
            print(f"Goodbye")
            break

        action = actions.get(choice)
        if action:
            action(records)
        else:
            print("Invalid menu option. Choose a number from 1 to 6.")


if __name__ == "__main__":

    main()
