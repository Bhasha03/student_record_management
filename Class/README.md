# Student Record Manager

A simple CRUD application for classroom demonstration. Student records are read from and saved to `student_records.json`.

## Features

- **Create:** Add a student with a unique roll number.
- **Read:** View all saved records or search by roll number.
- **Update:** Change a student's name, course, or mark.
- **Delete:** Remove a record after confirming the selection.

## Run the app

Open PowerShell in the project folder and run:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The browser will open automatically. Stop the application with `Ctrl+C` in PowerShell if needed.
