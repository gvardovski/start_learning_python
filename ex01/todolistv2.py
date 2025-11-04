import sys


def create_file(path):
    file = open(path, "w")
    file.write(
        "|----------|--------|---------------------------------------------------------------------------|\n")
    file.write(
        "| PRIORITY | STATUS |                                   TASK                                    |\n")
    file.write(
        "|----------|--------|---------------------------------------------------------------------------|\n")
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
            choise = choise.upper().strip()
            if choise == "Q":
                sys.exit("\nBye Bye!")
            elif choise == "Y":
                create_file(path)
            else:
                type_choise()
        type_choise()


def take_file_name():
    filename = input("\nPlease enter your tasks file name .txt or .json\n")
    filename = filename.lower().strip()
    if (filename.find(".txt", len(filename) - 4) == -1 or len(filename) <= 4) and (filename.find(".json", len(filename) - 5) == -1 or len(filename) <= 5):
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
    priority = ""
    status = ""

    def choose_priority():
        nonlocal priority
        decision = input("\nChoose priority!\n1 : High\n2 : Midl\n3 : Low\n")
        decision = decision.strip()
        if decision == "1":
            priority = "HIG"
        elif decision == "2":
            priority = "MID"
        elif decision == "3":
            priority = "LOW"
        else:
            choose_priority()

    def choose_status():
        nonlocal status
        decision = input("\nChoose status!\n1 : Finished\n2 : In process\n")
        decision = decision.strip()
        if decision == "1":
            status = "FIN"
        elif decision == "2":
            status = "PRO"
        else:
            choose_status()
    choose_priority()
    choose_status()
    task = input("\nPlease input task\n")
    while task == "":
        task = input("Please input task\n")
    file.write(f"|   {priority}    |  {status}   | {task.strip()}\n")
    file.write(
        "|----------|--------|---------------------------------------------------------------------------|\n")
    file.close()
    user_make_decision(path)


def find_task(path):
    text = input("Type keyword for search!\n")
    if text == "":
        find_task(path)
    file = open(path, 'r')
    print("|----------|--------|---------------------------------------------------------------------------|\n", end="")
    print("| PRIORITY | STATUS |                                   TASK                                    |\n", end="")
    print("|----------|--------|---------------------------------------------------------------------------|\n", end="")
    for line in file:
        if line.find(text) != -1:
            print(line, end="")
            print("|----------|--------|---------------------------------------------------------------------------|\n", end="")
    file.close()
    user_make_decision(path)


def save_to_file(path):
    decision = input(
        "\n1 : Save to file\n2 : Save to another file .txt\n3 : Save to another file .json\n")
    decision = decision.strip()
    if decision not in ["1", "2", "3"]:
        print("Please make correct choise!")
        save_to_file(path)
    elif decision in ["2", "3"]:
        def save_to_file_format(path):
            nonlocal decision
            filename = input("Enter file name\n")
            if filename == "":
                save_to_file_format(path)
            filename = filename.strip()
            file = open(path, "r")
            content = file.read()
            file.close()
            if decision == "2":
                file = open("data/" + filename + ".txt", "w")
            else:
                file = open("data/" + filename + ".json", "w")
            file.write(content)
            file.close()
        save_to_file_format(path)
    sys.exit("\nFile saved! Bye!")


def user_make_decision(path):
    decision = input(
        "\n1 : Add new task\n2 : View all tasks\n3 : Search for task by keyward\n4 : Save to file\n5 : Exit\n")
    decision = decision.strip()
    if decision not in ["1", "2", "3", "4", "5"]:
        print("Please make correct choise!")
        user_make_decision(path)
    elif decision == "2":
        print_tasks(path)
    elif decision == "1":
        add_task(path)
    elif decision == "3":
        find_task(path)
    elif decision == "4":
        save_to_file(path)
    elif decision == "5":
        sys.exit("\nBye Bye!")


if __name__ == "__main__":
    filename = take_file_name()
    path = "data/" + filename
    check_if_file_exist(path)
    user_make_decision(path)
