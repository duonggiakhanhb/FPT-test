from faker import Faker
import random
from datetime import datetime, timedelta
import sqlite3
from create_table import create_table

fake = Faker()

# Connect to SQLite database (creates if doesn't exist)
conn = sqlite3.connect('db/university.db')
cursor = conn.cursor()

# Create tables
create_table(conn, cursor)

# Generate Departments
for i in range(1, 6):
    cursor.execute("INSERT INTO Departments (dept_id, dept_name) VALUES (?, ?)", (i, fake.word() + " Department"))

# Generate Courses
for i in range(1, 11):
    cursor.execute("INSERT INTO Courses (course_id, course_name, dept_id) VALUES (?, ?, ?)",
                   (i, fake.job() + " Course", random.randint(1, 5)))

# Generate Students
for i in range(1, 21):
    cursor.execute("INSERT INTO Students (student_id, student_name, birthdate, dept_id) VALUES (?, ?, ?, ?)",
                   (i, fake.name(), fake.date_of_birth(minimum_age=18, maximum_age=25), random.randint(1, 5)))

# Generate Professors
for i in range(1, 6):
    cursor.execute("INSERT INTO Professors (professor_id, professor_name, dept_id) VALUES (?, ?, ?)",
                   (i, fake.name(), random.randint(1, 5)))

# Generate Enrollments
for i in range(1, 31):
    cursor.execute("INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES (?, ?, ?, ?)",
                   (i, random.randint(1, 20), random.randint(1, 10), fake.date_between(start_date='-1y', end_date='today')))

# Generate Teaches
for i in range(1, 11):
    cursor.execute("INSERT INTO Teaches (teaches_id, professor_id, course_id) VALUES (?, ?, ?)",
                   (i, random.randint(1, 5), random.randint(1, 10)))

# Generate Assignments
for i in range(1, 21):
    cursor.execute("INSERT INTO Assignments (assignment_id, assignment_name, course_id, deadline) VALUES (?, ?, ?, ?)",
                   (i, fake.catch_phrase(), random.randint(1, 10), fake.date_between(start_date='today', end_date='+60d')))

# Generate Grades
for i in range(1, 31):
    cursor.execute("INSERT INTO Grades (grade_id, enrollment_id, assignment_id, grade) VALUES (?, ?, ?, ?)",
                   (i, random.randint(1, 30), random.randint(1, 20), round(random.uniform(60, 100), 2)))

# Commit changes and close connection
conn.commit()
conn.close()

print("Data generated successfully.")
