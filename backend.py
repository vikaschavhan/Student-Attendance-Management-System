import sqlite3

# Define the database name and create the connection
db_name = "attendance.db"
conn = sqlite3.connect(db_name)

# Create the student table if it doesn't exist
conn.execute('''CREATE TABLE IF NOT EXISTS students
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 NAME TEXT NOT NULL,
                 EMAIL TEXT NOT NULL UNIQUE,
                 PASSWORD TEXT NOT NULL)''')

# Create the attendance table if it doesn't exist
conn.execute('''CREATE TABLE IF NOT EXISTS attendance
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 STUDENT_ID INTEGER NOT NULL,
                 DATE TEXT NOT NULL,
                 STATUS TEXT NOT NULL,
                 FOREIGN KEY (STUDENT_ID) REFERENCES students(ID))''')


# Define the function for adding a new student
def add_student(name, email, password):
    conn.execute("INSERT INTO students (NAME, EMAIL, PASSWORD) VALUES (?, ?, ?)", (name, email, password))
    conn.commit()


# Define the function for checking a student's login credentials
def check_login(email, password):
    cursor = conn.execute("SELECT * FROM students WHERE EMAIL = ? AND PASSWORD = ?", (email, password))
    student = cursor.fetchone()
    return student


# Define the function for adding attendance data for a student
def add_attendance(student_id, date, status):
    conn.execute("INSERT INTO attendance (STUDENT_ID, DATE, STATUS) VALUES (?, ?, ?)", (student_id, date, status))
    conn.commit()


# Define the function for getting attendance data for a student
def get_attendance(student_id):
    cursor = conn.execute("SELECT * FROM attendance WHERE STUDENT_ID = ?", (student_id,))
    attendance_data = cursor.fetchall()
    return attendance_data
