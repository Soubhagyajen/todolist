# Initialize an empty list for tasks
tasks = []

# Define functions for adding, listing, marking, and deleting tasks
def add_task(task):
    tasks.append(task)

def list_tasks():
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def mark_task_complete(index):
    tasks[index-1] = f"[DONE] {tasks[index-1]}"

def delete_task(index):
    del tasks[index-1]

# Main program loop
while True:
    print("\nTo-Do List:")
    list_tasks()

    print("\nOptions:")
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        task = input("Enter task description: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        index = int(input("Enter task number to mark complete: "))
        mark_task_complete(index)
    elif choice == "4":
        index = int(input("Enter task number to delete: "))
        delete_task(index)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

print("\nExiting program. Have a productive day!")
