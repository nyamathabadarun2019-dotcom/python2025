# a simple to do list

tasks = []

while True:
    print("\n1.Add Task  2.View Tasks  3.Remove Task  4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == 2:
        print("Your Tasks:", tasks)
    elif choice == 3:
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("Task not found")
    elif choice == 4:
        break
    else:
        print("Invalid choice")