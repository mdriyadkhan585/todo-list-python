# 📝 To-Do List Application
---
[In Python GUI](https://github.com/mdriyadkhan585/todo-list-GUI)


[In C Script](https://github.com/mdriyadkhan585/todo-list)


![Logo](logo.svg)

---
Welcome to the Python To-Do List Application! This program allows you to manage your tasks using a simple command-line interface, with tasks stored in an SQLite database for persistence.

## 📋 Features

- **Add Tasks** 🆕: Easily add tasks to your to-do list.
- **View Tasks** 📋: Display all tasks in a clear, formatted list.
- **Delete Tasks** 🗑️: Remove tasks from your list.
- **Persistent Storage** 💾: Tasks are saved in an SQLite database to ensure data is retained between sessions.

## 📦 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Code Structure](#code-structure)
5. [Troubleshooting](#troubleshooting)
6. [License](#license)

## 📋 Prerequisites

Before running the application, ensure you have:

- **Python** (version 3.x recommended)
- **SQLite** (Python’s `sqlite3` module is included with standard Python distributions)

## 🚀 Installation

1. **Clone the Repository** (or download the source code):

   ```sh
   git clone https://github.com/mdriyadkhan585/todo-list-python.git
   cd todo-list-python
   ```

2. **No Additional Packages Needed**: The script uses built-in Python libraries.

## 📖 Usage

Run the Python script with:

```sh
python todo_list.py
```

### Main Menu Options

1. **Add Task** 🆕
   - Enter the task description when prompted.
   - The task will be added to the list.

2. **View Tasks** 📋
   - Displays all current tasks with their respective IDs.

3. **Delete Task** 🗑️
   - First, view the tasks to get the ID of the task you want to delete.
   - Enter the task ID to remove it from the list.

4. **Exit** 🚪
   - Exits the program.

## 🔧 Code Structure

- **`todo_list.py`**: Contains the main program logic including database operations and user interface.
  - `open_database()`: Opens the SQLite database.
  - `create_table(conn)`: Creates the tasks table if it does not exist.
  - `add_task(conn, task)`: Adds a new task to the database.
  - `view_tasks(conn)`: Retrieves and displays all tasks.
  - `delete_task(conn, task_id)`: Deletes a task based on its ID.
  - `main()`: Manages user interaction and menu options.

## 🛠️ Troubleshooting

- **"No tasks to show"**: Indicates that no tasks are present in the database. Add tasks to see them listed.
- **"Invalid task number"**: Make sure to enter a valid task ID when deleting tasks. IDs are integers.
- **"Failed to add task"**: Check for issues in task input or database connection.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🧑‍💻 Contributing

Feel free to contribute by submitting issues or pull requests on the [GitHub repository](https://github.com/mdriyadkhan585/todo-list-python).

---
