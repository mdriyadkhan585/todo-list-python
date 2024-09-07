import sqlite3

DATABASE = 'todo_list.db'

def open_database():
    return sqlite3.connect(DATABASE)

def create_table(conn):
    with conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        );
        """)

def add_task(conn, task):
    with conn:
        conn.execute("INSERT INTO tasks (task) VALUES (?);", (task,))

def view_tasks(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, task FROM tasks;")
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks to show.")
    else:
        print("\n=== Tasks ===")
        for task in tasks:
            print(f"{task[0]}. {task[1]}")
        print("=============")

def delete_task(conn, task_id):
    with conn:
        conn.execute("DELETE FROM tasks WHERE id = ?;", (task_id,))

def main():
    conn = open_database()
    create_table(conn)

    while True:
        print("\n=== Todo List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        print("======================")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(conn, task)
            print("Task added successfully.")

        elif choice == '2':
            view_tasks(conn)

        elif choice == '3':
            view_tasks(conn)
            try:
                task_id = int(input("Enter task number to delete: "))
                delete_task(conn, task_id)
                print("Task deleted successfully.")
            except ValueError:
                print("Invalid task number.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    conn.close()

if __name__ == "__main__":
    main()
  
