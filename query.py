import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('db/university.db')
cursor = conn.cursor()

# Define the complex SQL query

# Top 1 of department based on their average grades
# Explaintion of the query:
# 1. Calculate the average grade of each course
# 2. Calculate the average grade of each department
# 3. Sort the departments by their average grade in descending order
purpose_1 = "Top 1 of department based on their average grades"
complex_query_1 = """
SELECT d.dept_id, d.dept_name, AVG(avg_course_grade) AS avg_department_grade
FROM Departments d
JOIN (
    SELECT c.dept_id, AVG(g.grade) AS avg_course_grade
    FROM Courses c
    JOIN Enrollments e ON c.course_id = e.course_id
    JOIN Grades g ON e.enrollment_id = g.enrollment_id
    GROUP BY c.course_id
) AS course_grades ON d.dept_id = course_grades.dept_id
GROUP BY d.dept_id, d.dept_name
ORDER BY avg_department_grade DESC;
"""

# This query aims to find the top-performing students in each department based on their average grades
# Explaintion of the query:
# 1. Calculate the average grade of each student in each department
# 2. Filter out the students with an average grade less than 90
# 3. Sort the students by their average grade in descending order by department
purpose_2 = "Top-performing students in each department based on their average grades and grade >= 90"
complex_query_2 = """
SELECT s.student_id, s.student_name, d.dept_name, AVG(avg_course_grade) AS avg_student_grade
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
JOIN Departments d ON c.dept_id = d.dept_id
JOIN (
    SELECT e.student_id, c.dept_id, AVG(g.grade) AS avg_course_grade
    FROM Enrollments e
    JOIN Courses c ON e.course_id = c.course_id
    JOIN Grades g ON e.enrollment_id = g.enrollment_id
    GROUP BY e.student_id, c.dept_id
) AS student_dept_grades ON s.student_id = student_dept_grades.student_id AND d.dept_id = student_dept_grades.dept_id
GROUP BY s.student_id, s.student_name, d.dept_id, d.dept_name
HAVING avg_student_grade >= 90
ORDER BY d.dept_id, avg_student_grade DESC;
"""

# Top 1 of each course based on their highest grades
# Explaintion of the query:
# 1. Calculate the highest grade of each course
purpose_3 = "Top 1 of course based on their highest grades"
complex_query_3 = """
SELECT s.student_id, s.student_name, c.course_name, g.grade AS highest_grade
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
JOIN (
    SELECT e.course_id, MAX(g.grade) AS max_grade
    FROM Grades g
    JOIN Enrollments e ON g.enrollment_id = e.enrollment_id
    GROUP BY e.course_id
) AS max_grades ON e.course_id = max_grades.course_id
JOIN Grades g ON e.enrollment_id = g.enrollment_id AND g.grade = max_grades.max_grade;
"""

def run_query(query, purpose=""):
    cursor.execute(query)
    results = cursor.fetchall()
    print(f"Query Purpose: {purpose}")
    for row in results:
        print(row)
    print(f"Total rows: {len(results)}\n")

# Run the query
run_query(complex_query_1, purpose_1)
run_query(complex_query_2, purpose_2)
run_query(complex_query_3, purpose_3)

# Close connection
conn.close()
