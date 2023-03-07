from tkinter import *
from tkinter import messagebox
from backend import *

# Define the main window
root = Tk()
root.title("Student Attendance Management System")


# Define the functions for the login and registration screens
def login_screen():
    # Define the login screen
    login_window = Toplevel(root)
    login_window.title("Login")
    login_window.geometry("300x200")

    # Define the login fields and labels
    email_label = Label(login_window, text="Email:")
    email_label.pack()
    email_entry = Entry(login_window)
    email_entry.pack()
    password_label = Label(login_window, text="Password:")
    password_label.pack()
    password_entry = Entry(login_window, show="*")
    password_entry.pack()

    # Define the login function
    def login():
        email = email_entry.get()
        password = password_entry.get()
        student = check_login(email, password)
        if student:
            attendance_screen(student[0])
            login_window.destroy()
        else:
            messagebox.showerror("Error", "Invalid email or password")

    # Define the login button
    login_button = Button(login_window, text="Login", command=login)
    login_button.pack()


def registration_screen():
    # Define the registration screen
    registration_window = Toplevel(root)
    registration_window.title("Registration")
    registration_window.geometry("300x250")

    # Define the registration fields and labels
    name_label = Label(registration_window, text="Name:")
    name_label.pack()
    name_entry = Entry(registration_window)
    name_entry.pack()
    email_label = Label(registration_window, text="Email:")
    email_label.pack()
    email_entry = Entry(registration_window)
    email_entry.pack()
    password_label = Label(registration_window, text="Password:")
    password_label.pack()
    password_entry = Entry(registration_window, show="*")
    password_entry.pack()


# Define the login and registration buttons in the main window
login_button = Button(root, text="Login", command=login_screen)
login_button.pack()
registration_button = Button(root, text="Register", command=registration_screen)
registration_button.pack()

root.mainloop()
