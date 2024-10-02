# Simple To-Do List Application

def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour To-Do List is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{idx}. {task['task']} - {status}")

def add_task(tasks):
    task_name = input("Enter the task name: ")
    tasks.append({"task": task_name, "completed": False})
    print(f"Task '{task_name}' added successfully.")

def update_task(tasks):
    if not tasks:
        print("Your To-Do List is empty.")
        return
    
    view_tasks(tasks)
    task_num = int(input("Enter the task number to update: "))
    
    if 1 <= task_num <= len(tasks):
        new_task_name = input("Enter the new task name: ")
        tasks[task_num - 1]["task"] = new_task_name
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def mark_task_completed(tasks):
    if not tasks:
        print("Your To-Do List is empty.")
        return
    
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: "))
    
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        print(f"Task '{tasks[task_num - 1]['task']}' marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    if not tasks:
        print("Your To-Do List is empty.")
        return
    
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task['task']}' deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            mark_task_completed(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            print("Exiting the To-Do List Application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
