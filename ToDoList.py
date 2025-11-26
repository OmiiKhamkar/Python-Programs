# Simple To-Do List App

FILENAME = "tasks.txt"

def add_task(task):
    with open(FILENAME, "a") as file:
        file.write(task + "\n")
    print("Task added!")

def view_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found.")

def delete_task(task_no):
    with open(FILENAME, "r") as file:
        tasks = file.readlines()

    if 0 < task_no <= len(tasks):
        tasks.pop(task_no - 1)
        with open(FILENAME, "w") as file:
            file.writelines(tasks)
        print("Task deleted!")
    else:
        print("Invalid task number.")

while True:
    print("\n--- To-Do Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        add_task(task)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        delete_task(num)

    elif choice == "4":
        break

    else:
        print("Invalid option! Try again.")
