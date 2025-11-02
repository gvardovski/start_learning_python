import sys

def create_file(path):
    file = open(path, "w")
    file.write("|----------|--------|---------------------------------------------------------------------------|\n")
    file.write("| PRIORITY | STATUS |                                                                           |\n")
    file.write("|----------|--------|---------------------------------------------------------------------------|\n")
    file.close()

def check_if_file_exist(path):
    try:
        with open(path, "r") as file:
            content = file.read()
            print("\nFound your tasks!")
            file.close()
    except FileNotFoundError:
        print("\nYour TO DO LIST doesn't exist yet!\nDo you want to create it?")
        def type_choise():
            choise = input("\nType\nY if YES\nQ if NO\n")
            if choise.upper() == "Q":
                sys.exit("\nBye Bye!")
            elif choise.upper() == "Y":
                create_file(path)
            else:
                type_choise()
        type_choise()

def take_file_name():
    filename = input("\nPlease enter your tasks file name .txt or .json\n")
    filename = filename.lower()
    if (filename.find(".txt", len(filename) - 4) == -1 or len(filename) <= 4 ) and (filename.find(".json", len(filename) - 5) == -1 or len(filename) <= 5):
        print("Extension should be .txt or .json! Try again!")
        filename = take_file_name()
    else:
        return filename
    return filename

def print_tasks(path):
    file = open(path, "r")
    for line in file:
        print(line, end="")
    file.close()
    user_make_decision(path)

def add_task(path):
    file = open(path, "a")
    input("\nChoose priority!\n1 : High\n2 : Midl\n3 : Low")
    if input not in ["1", "2", "3"]:
        priority = ""
    
    file.close()
    user_make_decision(path)

def user_make_decision(path):
    decision = input("\n1 : Add new task\n2 : View all tasks\n3 : Search for task by keyward\n4 : Save to file\n5 : Exit\n")
    if decision not in ["1", "2", "3", "4", "5"]:
        print("Please make correct choise!")
        user_make_decision(path)
    elif decision == "2":
        print_tasks(path)
    elif decision == "1":
        add_task(path)
    elif decision == "5":
        sys.exit("\nBye Bye!")

filename = take_file_name()
path = "data/" + filename
check_if_file_exist(path)
user_make_decision(path)