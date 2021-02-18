import time
print("Welcome to to-do-list")
name = input("What is your name? : ")

tasks = []
def new_tasks():
    repeat = True
    while repeat == True:
        new = input("Please enter a new task or type end to stop : ").strip() .lower()
        if new == 'end':
            menu()
        else:
            tasks.append(new)


def view_tasks():
    for new in tasks:
        time.sleep(0.5)
        
        print(" , ".join(tasks))
        time.sleep(0.5)
        print("------------------------------")
        
        time.sleep(1.5)
        menu()
        
        
def menu():
    print("Hi {} Choose a mode by entering the number: ".format(name))
    while True:
        try:
            number = int(input("""
1: Add a task 
2: View list
3: Exit
Enter : """))
            break
        # Print an error message if there is any error
        except ValueError:
            print("Please enter a number, from 1 to 3.")
            return number
            
    # if statements which go with relevant numbers and functions
    if number == 1:
        new_tasks()
    
    elif number == 2:
        view_tasks()
        
    elif number == 3:
        print("Goodbye")
        time.sleep(1)
        # exit the code if chosen
        exit()

menu()

