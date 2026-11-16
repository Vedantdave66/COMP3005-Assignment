"""Simple PostgreSQL CRUD demonstration for the students table."""

import os
from datetime import date

import psycopg


def connect():
    """Open a connection using the local PostgreSQL configuration."""
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "comp3005_assignment"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.environ["DB_PASSWORD"],
    )


def getAllStudents():
    """Retrieve and print every student."""
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM students ORDER BY student_id")
            students = cur.fetchall()

    for student in students:
        print(student)
    return students


def addStudent(first_name, last_name, email, enrollment_date):
    """Insert a student and return the generated student ID."""
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """INSERT INTO students (first_name, last_name, email, enrollment_date)
                   VALUES (%s, %s, %s, %s) RETURNING student_id""",
                (first_name, last_name, email, enrollment_date),
            )
            student_id = cur.fetchone()[0]
    print(f"Added student {student_id}")
    return student_id


def updateStudentEmail(student_id, new_email):
    """Update one student's email and report whether the ID exists."""
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE students SET email = %s WHERE student_id = %s",
                (new_email, student_id),
            )
            updated = cur.rowcount
    print("Email updated" if updated else "Student not found")
    return updated


def deleteStudent(student_id):
    """Delete one student and report whether the ID exists."""
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
            deleted = cur.rowcount
    print("Student deleted" if deleted else "Student not found")
    return deleted


def main():
    """Run each required operation in a predictable demonstration sequence."""
    try:
        print("\n1. Initial students")
        getAllStudents()

        print("\n2. Add student")
        new_id = addStudent("Alex", "Taylor", "alex.taylor@example.com", date(2026, 9, 1))
        getAllStudents()
        input("Check the inserted student in pgAdmin, then press Enter...")

        print("\n3. Update email")
        updateStudentEmail(new_id, "alex.updated@example.com")
        getAllStudents()
        input("Check the updated email in pgAdmin, then press Enter...")

        print("\n4. Delete student")
        deleteStudent(new_id)
        getAllStudents()
        input("Check the deleted student in pgAdmin, then press Enter to finish...")
    except (psycopg.Error, KeyError) as error:
        print(f"Database operation failed: {error}")


if __name__ == "__main__":
    main()
