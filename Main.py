import sys

def addTask(task_to_add: str, due_date: str):
    with open("weekly_planner.txt", "w") as infile:   
        infile.write(f"{task_to_add}, Due: {due_date}\n")
        print(f"Task:{task_to_add} has been added!")
    return addTask
    

def deleteTask(task_to_delete):
    with open("weekly_planner.txt", "r") as r:
        lines = r.readlines()
    with open("weekly_planner.txt", "w") as w:
        for row in lines:
            if row.find(task_to_delete) != -1:
                w.write("")
                print("your task has been deleted")
                return
            else:
                print("please check you entered the task name and due data exactly, and try again")
                return
                
active = True 
while active == True:
    decision = input("Welcome to your weekly planner! Please enter 1 to add a task, enter 2 to delete a task, 3 to view your diary or 4 to exit the program")
    if decision == "1":
        task_to_add = input("please enter the task name")
        due_date = input("please enter the task due date")
        addTask(task_to_add, due_date)
    elif decision == "2":
        task_to_delete = input("please enter the exact name of the task and its due data, if you cannot remember the name, restart the program and chose view planner to find the name")
        deleteTask(task_to_delete)
    elif decision == "3":
        with open ("weekly_planner.txt", "r") as f:
            print(f.read())
    elif decision == "4":
        active = False
        sys.exit("see you next time :)")
    else:
        print("please restart, and enter one of the options given")
  
    
