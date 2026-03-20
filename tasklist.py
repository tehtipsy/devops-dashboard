tasks = []


def manage_tasks():
    while True:
        print("\n--- Task List ---")
        print("[1] Add a task")
        print("[2] View all tasks")
        print("[3] Remove a task")
        print("[0] Return to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == "2":
            if not tasks:
                print("No tasks.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"  {i}. {task}")
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"  {i}. {task}")
                num = input("Enter task number to remove: ")
                try:
                    index = int(num) - 1
                    if 0 <= index < len(tasks):
                        removed = tasks.pop(index)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Try again.")
