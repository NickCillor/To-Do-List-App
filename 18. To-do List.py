def tasks():
    tasks_list = []
    task_num = int(input("Enter the number of tasks you want: "))
    for i in range(1, task_num + 1):
        task_name = input(f"Enter task {i}: ")
        tasks_list.append(task_name)
    print("Your tasks are:")
    for task in tasks_list:
        print("-", task)

    while True:
        print("\nEnter:")
        print("1 to add a task,\n2 to remove a task,\n3 to update a task,\n4 to view tasks,\n5 to exit: ")
        task_settings = int(input("Enter your choice: "))

        if task_settings == 1:
            task_name_add = input("Enter the task you want to add: ")
            tasks_list.append(task_name_add)
            print(f"Task {task_name_add} added successfully.")

        elif task_settings == 2:
            task_name_remove = input("Enter the task you want to remove: ")
            if task_name_remove in tasks_list:
                tasks_list.remove(task_name_remove)
                print("Task removed.")
            else:
                print("Task not found.")

        elif task_settings == 3:
            old_task = input("Enter the task you want to update: ")
            if old_task in tasks_list:
                new_task = input("Enter the new task: ")
                index = tasks_list.index(old_task)
                tasks_list[index] = new_task
                print("Task updated.")
            else:
                print("Task not found.")

        elif task_settings == 4:
            print("\nCurrent tasks:")
            for task in tasks_list:
                print("-", task)

        elif task_settings == 5:
            print("Exiting task manager.")
            break

        else:
            print("Invalid option. Try again.")

tasks()

