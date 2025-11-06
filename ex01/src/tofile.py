import sys
import json
import todolistv2


def save_to_file(content, path):
    decision = input(
        "\n1 : Save to file\n2 : Save to another file .txt\n3 : Save to another file .json\n")
    decision = decision.strip()
    if decision not in ["1", "2", "3"]:
        print("Please make correct choise!")
        save_to_file(content)
    elif decision == "1":
        def choose_format(content):
            with open(path, "w") as file:
                if path.find(".txt", len(path) - 4):
                    file.write(str(content).replace("\'", "\""))
                else:
                    json.dump(content, file, indent=4)
        choose_format(content)
    else:
        def save_to_file_format(content):
            nonlocal decision
            filename = input("Enter file name\n")
            if filename == "":
                save_to_file_format(content)
            filename = filename.strip()
            if decision == "2":
                with open("data/" + filename + ".txt", "w") as file:
                    file.write(str(content).replace("\'", "\""))
            else:
                with open("data/" + filename + ".json", "w") as file:
                    json.dump(content, file, indent=4)
        save_to_file_format(content)
    print("\nFile saved!")
    todolistv2.user_make_decision(content, path)
