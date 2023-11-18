

def create_table(conn, cursor):
    
    # Create Departments Table
    cursor.execute('''
        CREATE TABLE Departments (
            dept_id INTEGER PRIMARY KEY,
            dept_name TEXT NOT NULL
        )
    ''')

    # Create Courses Table
    cursor.execute('''
        CREATE TABLE Courses (
            course_id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL,
            dept_id INTEGER,
            FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
        )
    ''')

    # Create Students Table
    cursor.execute('''
        CREATE TABLE Students (
            student_id INTEGER PRIMARY KEY,
            student_name TEXT NOT NULL,
            birthdate DATE,
            dept_id INTEGER,
            FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
        )
    ''')

    # Create Enrollments Table
    cursor.execute('''
        CREATE TABLE Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            enrollment_date DATE,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        )
    ''')

    # Create Professors Table
    cursor.execute('''
        CREATE TABLE Professors (
            professor_id INTEGER PRIMARY KEY,
            professor_name TEXT NOT NULL,
            dept_id INTEGER,
            FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
        )
    ''')

    # Create Teaches Table
    cursor.execute('''
        CREATE TABLE Teaches (
            teaches_id INTEGER PRIMARY KEY,
            professor_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (professor_id) REFERENCES Professors(professor_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        )
    ''')

    # Create Assignments Table
    cursor.execute('''
        CREATE TABLE Assignments (
            assignment_id INTEGER PRIMARY KEY,
            assignment_name TEXT NOT NULL,
            course_id INTEGER,
            deadline DATE,
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        )
    ''')

    # Create Grades Table
    cursor.execute('''
        CREATE TABLE Grades (
            grade_id INTEGER PRIMARY KEY,
            enrollment_id INTEGER,
            assignment_id INTEGER,
            grade DECIMAL(3, 2),
            FOREIGN KEY (enrollment_id) REFERENCES Enrollments(enrollment_id),
            FOREIGN KEY (assignment_id) REFERENCES Assignments(assignment_id)
        )
    ''')

    # Commit changes and close connection
    conn.commit()

    print("Tables created successfully.")
