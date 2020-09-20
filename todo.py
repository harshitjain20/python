todo = []
complete = []
while True:
    print("select the option")
    print("1 for Add new task")
    print("2 for View all tasks")
    print("3 for complete the task")
    print("4 for view Completed tasks")
    print("5 for clear all tasks")
    choice = int(input())
    if choice == 1:
        task = input("Enter the task \n")
        todo.append(task)
    elif choice == 2:
        if len(todo) >0:
            print("Pending tasks are :")
            for i in range(len(todo)):
                print(f"{i+1} - {todo[i]}")
        else:
            print("No Tasks pending")
    elif choice == 3:
        print("Select the following task you have completed..!!")
        for i in range(len(todo)):
            print(f"{i+1} - {todo[i]}")
        taskind = int(input())
        complete.append(todo[taskind-1])
        todo.pop(taskind-1)
    elif choice == 4:
        if len(complete) >0:
            print("you have completed the following task")
            for i in range(len(complete)):
                print(f"{i+1} - {complete[i]}")
        else:
            print("No tasks you have completed yet...!!")
    elif choice == 5:
        todo.clear()
        print("All tasks are cleared...!!!")
    else:
        print("invalid input")
    print("Do you want continue [Y/N]")
    again = input()
    if again.lower() == "n":
        break;