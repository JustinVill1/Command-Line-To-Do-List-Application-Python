
tasks = []

def Addtasks():
    task = input("What task would you like to add?:")
    tasks.append(task)
    print(f"'{task}' has been added.")
    print(f"Current tasks: {task}")
    
def DeleteTasks():
    listTasks()
    try:
        tasktodelete = int(input("What task number would you like to remove?: "))
        if tasktodelete >= 0 and tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print(f"Task {tasktodelete} has been removed.")
        else:
            print(f"Task #{tasktodelete} was not found")
    except:
        print("Invalid input")


def listTasks():
    if not tasks:
        print("There are no tasks")
    else:
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")


# This is the main method
# This is saying that if this file is the only one being ran, to run the code corresponding it
if __name__ == "__main__":
        

    #Creating the loop to run the app
    print("Welcome to To-Do List.")

    while True:
        print("\nSelect one of the following options.")
        print("------------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        UserChoice = input("Enter your choice: ")

        if (UserChoice == "1"):
            Addtasks()
        elif (UserChoice == "2"):
            DeleteTasks()
        elif (UserChoice == "3"):
            listTasks()
        elif (UserChoice == "4"):
            break
        else:
            print("Invalid. Enter a choice")