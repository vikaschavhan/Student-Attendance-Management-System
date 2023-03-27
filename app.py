import streamlit as st
import pandas as pd


def main():
    st.title("Student Attendance Management System")
    menu = ["Home", "View Attendance", "Add Attendance", "View Students", "Add Students"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to the Student Attendance Management System.")
        st.write("Please select an option from the sidebar.")

    elif choice == "View Attendance":
        st.subheader("View Attendance")
        df = pd.read_csv("attendance.csv", sep=',')
        st.dataframe(df)

    elif choice == "Add Attendance":
        st.subheader("Add Attendance")
        student_id = st.text_input("Enter the student ID:")
        date = st.text_input("Enter the date (yyyy-mm-dd):")
        present = st.checkbox("Present?")
        if st.button("Submit"):
            with open("attendance.csv", "a") as f:
                f.write(f"{student_id},{date},{present}\n")
            st.success("Attendance added successfully.")

    elif choice == "View Students":
        st.subheader("View Students")
        df = pd.read_csv("students.csv", sep=',')
        st.dataframe(df)

    elif choice == "Add Students":
        st.subheader("Add Students")
        name = st.text_input("Enter the student name:")
        student_id = st.text_input("Enter the student ID:")
        if st.button("Submit"):
            with open("students.csv", "a") as f:
                f.write(f"{name},{student_id}\n")
            st.success("Student added successfully.")


if __name__ == "__main__":
    main()
