import sys
import json
from src import tasks
from src import tofile


def create_file(path):
    file = open(path, "w")
    file.close()


def check_if_file_exist(path):
    try:
        with open(path, "r") as file:
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


def user_make_decision(content, path):
    decision = input(
        "\n1 : Add new task\n2 : View all tasks\n3 : Search for task by keyward\n4 : Save to file\n5 : Exit\n")
    decision = decision.strip()
    if decision not in ["1", "2", "3", "4", "5"]:
        print("Please make correct choise!")
    elif decision == "2":
        tasks.print_tasks(content)
    elif decision == "1":
        tasks.add_task(content)
    elif decision == "3":
        tasks.find_task(content)
    elif decision == "4":
        tofile.save_to_file(content, path)
    elif decision == "5":
        sys.exit("\nBye Bye!")
    user_make_decision(content, path)


def get_content_from_file(path):
    if path.find(".txt", len(filename) - 4):
        try:
            with open(path, "r") as file:
                content = file.read()
                file.close()
                if content == "":
                    return {}
                else:
                    return (json.loads(content))
        except FileNotFoundError:
            print("\nFile doesn't exist")
    else:
        try:
            with open(path, "r") as js_file:
                content = json.load(js_file)
                js_file.close()
                return content
        except FileNotFoundError:
            print("\nFile doesn't exist")


if __name__ == "__main__":
    filename = take_file_name()
    path = "data/" + filename
    check_if_file_exist(path)
    content = get_content_from_file(path)
    user_make_decision(content, path)
