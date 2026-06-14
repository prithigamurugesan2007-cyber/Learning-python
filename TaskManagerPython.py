tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter the task name: ").strip()

        if task == "":
            print("Task cannot be empty.")
        else:
            tasks.append(task)
            print(f"Task '{task}' added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                num = int(input("Enter task number to remove: "))

                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
