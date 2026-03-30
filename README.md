# 🎓 Student Management System

A simple Python-based Command Line Interface (CLI) tool to manage student records. This project demonstrates basic CRUD (Create, Read, Update, Delete) operations using lists and dictionaries.

## 🚀 Features

The system allows you to:
1. **Register Students:** Capture ID, name, age, course, and enrollment status.
2. **Consult Student List:** View all currently registered students in a formatted list.
3. **Search by ID:** Quickly find a specific student using their unique ID.
4. **Update Information:** Modify existing student data (keeping current values if fields are left blank).
5. **Delete Records:** Remove a student from the system via their ID.

## 🛠️ Requirements

*   **Python 3.x** or higher installed on your machine.

## 📁 Project Structure

*   `main.py`: Contains the main application loop and the interactive menu.
*   `functions.py`: Contains the core logic and functions for data manipulation.

## 💻 How to Run

1.  **Download** both `main.py` and `functions.py` into the same folder.
2.  Open your **terminal** or command prompt.
3.  Navigate to the project folder.
4.  Run the application using:
    ```bash
    python main.py
    ```

## ⚠️ Important Notes

*   **Data Persistence:** This version uses an **in-memory list**. This means all data will be cleared once the program is closed.
*   **Error Handling:** The registration process includes basic `try-except` blocks to prevent crashes from invalid data types (e.g., entering letters in the ID field).
