# COMP 3005 — PostgreSQL Students CRUD Assignment

A Python application that connects to PostgreSQL and performs Create, Read, Update, and Delete operations on a `students` table.

## Requirements

- PostgreSQL running locally
- pgAdmin 4
- Python 3.10 or newer

## Database setup

1. Open pgAdmin 4 and connect to the local PostgreSQL server.
2. Create a database named `comp3005_assignment` (right-click **Databases** → **Create** → **Database**).
3. Open **Query Tool** for `comp3005_assignment`.
4. Open `database/setup.sql` and execute it. This script drops and recreates the `students` table, so it will remove any existing data in that table.
5. Confirm that the three starting students appear in the query results.

## Run the application

From the project root directory, install the Python dependency:

```bash
python -m pip install -r requirements.txt
```

Set your local PostgreSQL password as an environment variable. **Do not commit your password to GitHub.**

Windows PowerShell:

```powershell
$env:DB_PASSWORD = "YOUR_POSTGRES_PASSWORD"
python app/main.py
```

macOS/Linux:

```bash
export DB_PASSWORD="YOUR_POSTGRES_PASSWORD"
python app/main.py
```

The application uses `localhost`, port `5432`, database `comp3005_assignment`, and user `postgres` by default. If yours differs, set `DB_HOST`, `DB_PORT`, `DB_NAME`, or `DB_USER` as environment variables.

## Functions

- `getAllStudents()` retrieves and prints all student records.
- `addStudent(first_name, last_name, email, enrollment_date)` inserts a student and returns the new ID.
- `updateStudentEmail(student_id, new_email)` updates an existing student's email.
- `deleteStudent(student_id)` removes a student record.

The demo adds a temporary student, updates their email, then deletes them. The three starting students remain afterward. SQL parameters are used to safely pass values into queries, and connection context managers handle commits, rollbacks, and cleanup.

## Video demonstration

**Video link:** (https://youtu.be/7FvfWSaT1yY)

In the video (maximum five minutes), show the database schema and initial records in pgAdmin, run `python app/main.py`, and use pgAdmin queries to verify the insert, update, and delete operations. The application pauses after INSERT, UPDATE, and DELETE so you can switch to pgAdmin, run `SELECT * FROM students ORDER BY student_id;`, and show each change before pressing Enter to continue. Re-run `setup.sql` before a fresh demonstration.

## Submission

Publish this project to a public GitHub repository. Add the video URL above, commit your changes, verify the link works for viewers without your account, and submit the repository URL in Brightspace.
