import sys
import json
import os
from src import tasks
from src import tofile

def check_if_file_exist(path):
    if os.path.exists(path):
        print("\nFound your tasks!")
    else:
        print("\nYour TO DO LIST doesn't exist yet!\nDo you want to create it?")

        def type_choise():
            choise = input("\nType\nY if YES\nQ if NO\n")
            choise = choise.upper().strip()
            if choise == "Q":
                sys.exit("\nBye Bye!")
            elif choise == "Y":
                with open(path, "w") as file:
                    file.write("{}")
            else:
                type_choise()
        type_choise()


def take_file_name():
    filename = input("\nPlease enter your tasks file name .txt or .json\n")
    filename = filename.lower().strip()
    if filename.split(".")[-1] != "txt" and filename.split(".")[-1] != "json":
        print("Extension should be .txt or .json! Try again!")
        filename = take_file_name()
    else:
        return filename
    return filename


def user_make_decision(content, path):
    decision = input(
        "\n1 : Add new task\n2 : View all tasks\n3 : Search for task by keyward\n4 : Save to file\n5 : Load file\n6 : Exit\n")
    decision = decision.strip()
    if decision not in ["1", "2", "3", "4", "5", "6"]:
        print("Please make correct choise!")
    elif decision == "1":
        tasks.add_task(content)
    elif decision == "2":
        tasks.print_tasks(content)
    elif decision == "3":
        tasks.find_task(content)
    elif decision == "4":
        tofile.save_to_file(content, path)
    elif decision == "5":
        main()
    elif decision == "6":
        sys.exit("\nBye Bye!")
    user_make_decision(content, path)


def get_content_from_file(path):
        with open(path, "r") as file:
            content = file.read()
            if content == "":
                return {}
            else:
                if path.split(".")[-1] == "txt":     
                    return json.loads(content)
                else:
                    with open(path, "r") as file:
                        return json.load(file)


def main():
    filename = take_file_name()
    path = "data/" + filename
    check_if_file_exist(path)
    content = get_content_from_file(path)
    user_make_decision(content, path)

if __name__ == "__main__":
    main()
