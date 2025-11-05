import sys
active = True 
while active == True:
    decision = input("Welcome to your weekly planner! Please enter 1 to add a task, enter 2 to delete a task, 3 to view your diary or 4 to exit the program")
    if decision == "1":
        task_to_add = input("please enter the task name")
        due_date = input("please enter the task due date")
        addTask(task_to_add, due_date)
    elif decision == "2":
        task_to_delete = input("please enter the exact name of the task, if you cannot remeber the name, restart the program and chose view planner to find the name")
        deleteTask(task_to_delete)
    elif decision == "3":
        with open ("weekly_planner.txt", "r") as f:
            print(f.read())
    elif decision == "4":
        sys.exit("see you next time :)")
    else:
        sys.exit("please restart, and enter one of the options given")


def addTask(task_to_add, due_date):{

}
    
def deleteTask(task_to_delete):{

}
    
