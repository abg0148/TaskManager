from auth import authenticate
from db import add_task, get_tasks, delete_task

def task_manager():
    print("Welcome to the Task Manager App!")

    if not authenticate():
        print("Authentication failed. Exiting...")
        return

    while True:
        print("\nOptions:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task description: ")
            add_task(task)
            print("Task added!")

        elif choice == '2':
            print("\nYour Tasks:")
            for task in get_tasks():
                print(f"{task['id']}: {task['description']}")
        
        elif choice == '3':
            task_id = input("Enter the task ID to delete: ")
            delete_task(task_id)
            print("Task deleted!")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid number.")

if __name__ == "__main__":
    task_manager()

