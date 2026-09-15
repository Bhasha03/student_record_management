""" Student Record Management System - Streamlit edition. """

import json
import streamlit as st


def load_records():
    """Return saved records. Start with an empty list if the file is new."""
    try:
        with open(r"C:\Users\bhava\Desktop\DA Course Material Day-Wise\Python\student_record_management\Class\student_data.json") as file:
            records = json.load(file)
        return records

    except FileNotFoundError:
        st.warning("No records file found. Starting with an empty record list.")
        return []
    except json.JSONDecodeError:
        st.error("The records file is not valid JSON. Starting with an empty record list.")
        return []

def save_records(records):
    """Save all records. Returns True only when saving succeeds."""

    with open(r"C:\Users\bhava\Desktop\DA Course Material Day-Wise\Python\student_record_management\Class\student_data.json", "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)
    return True


def find_record(records, roll_number): # Helper function to find a record by roll number
    """Return the matching record dictionary, or None when not found."""

    for record in records:
        if record["roll_number"] == roll_number:
            return record

    return None


def add_record(records):
    st.subheader("Add student")
    with st.form("add_student_form", clear_on_submit=True):

        roll_number = st.text_input("Roll number")
        name = st.text_input("Name").title()
        course = st.text_input("Course").title()
        mark = st.number_input("Mark (0-100)") # min_value=0, max_value=100, step=1

        submitted = st.form_submit_button("Add student")
 
    if submitted:
        
        roll_number = roll_number.strip()
        name = name.strip()
        course = course.strip()

        if not roll_number or not name or not course:
            st.warning("Value cannot be left empty.")
        elif find_record(records, roll_number):
            st.warning("A student with that roll number already exists.")
        else:
            record = {
                        "roll_number": roll_number,
                        "name": name.title(),
                        "course": course.title(),
                        "mark": int(mark),
                     }
            records.append(record)

            if save_records(records):
                st.success("Student record added and saved.")


def view_records(records):
    st.subheader("All students")
    if not records:
        st.info("No student records available.")
        return

    st.dataframe(records, hide_index=True)


def search_record(records):
    st.subheader("Search student")
    with st.form("search_student_form"):
        roll_number = st.text_input("Roll number")
        submitted = st.form_submit_button("Search")

    if submitted:
        roll_number = roll_number.strip()
        if not roll_number:
            st.warning("This value cannot be empty.")
            return

        record = find_record(records, roll_number)
        if record:
            st.write(f"Name   : {record['name']}")
            st.write(f"Course : {record['course']}")
            st.write(f"Mark   : {record['mark']}")
        else:
            st.info("Student record not found.")


def update_mark(records):
    st.subheader("Update mark")
    with st.form("update_mark_form"):
        roll_number = st.text_input("Roll number")
        mark = st.number_input("New mark (0-100)")
        submitted = st.form_submit_button("Update mark")

    if submitted:
        roll_number = roll_number.strip()
        if not roll_number:
            st.warning("This value cannot be empty.")
            return

        record = find_record(records, roll_number)
        if not record:
            st.info("Student record not found.")
            return

        record["mark"] = mark  
                                
        if save_records(records):
            st.success("Mark updated and saved.")

def exit():
    st.subheader("Goodbye :>")
    st.balloons()
    return


def show_menu():
    return st.sidebar.selectbox(
        "Choose an option",
        [
            "Add student",
            "View all students",
            "Search by roll number",
            "Update mark",
            "Exit"
        ]
    )


def main():
    # st.set_page_config(page_title="Student record management", layout="wide")
    st.title("Student Record Management System")

    records = load_records()
    choice = show_menu()

    actions = {
        "Add student": add_record,
        "View all students": view_records,
        "Search by roll number": search_record,
        "Update mark": update_mark, 
    }

    if choice == "Exit":
        exit()

    action = actions.get(choice)
    if action:
        action(records)


main()



# The full JSON type system:

# JSON type	                Example	       Python equivalent
# ================================================================
# object	                {"a": 1}	        dict
# array	                    [1, 2, 3]	        list
# string	                 "text"	            str
# number	                42 or 3.14	     int / float
# boolean	                true / false	True / False
# null	                       null	            None
