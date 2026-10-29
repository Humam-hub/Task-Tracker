# Mini Task Tracker

A menu-based Python command-line task manager that stores tasks persistently using a JSON file.

---

## 🎯 Project Goal
The goal of this project is to build a lightweight, robust CLI Task Tracker in Python that persists task data to a `tasks.json` file across program restarts, implementing error handling for edge cases such as missing files, invalid numbers, and blank inputs.

---

## ✨ Features
- **Add Task:** Add tasks with a title; automatically initialized as `[Pending]`.
- **View Tasks:** View all tasks numbered sequentially with their current status (`[Pending]` or `[Done]`).
- **Complete Task:** Select a task by its index number and update its status to `[Done]`.
- **Delete Task:** Remove a task by its index number.
- **Persistence:** Automatically loads data from `tasks.json` at startup and persists any updates after adding, completing, or deleting tasks.
- **Error Handling:**
  - Handles non-existent or corrupted `tasks.json` gracefully.
  - Prevents adding empty/blank task titles.
  - Catches invalid/non-numeric task selections and out-of-range task numbers.
  - Handles unrecognized menu inputs.

---

## 📂 Project Structure
```text
├── mini_task_tracker.py   # Main Python application
├── tasks.json             # Persistent storage file (generated on save)
└── README.md              # Project documentation
```
---
