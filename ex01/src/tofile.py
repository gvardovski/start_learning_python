import sys
import json


def save_to_file(content, path):
    decision = input(
        "\n1 : Save to file\n2 : Save to another file .txt\n3 : Save to another file .json\n")
    decision = decision.strip()
    if decision not in ["1", "2", "3"]:
        print("Please make correct choise!")
        save_to_file(content)
    elif decision == "1":
        def choose_format(content):
            if path.find(".txt", len(path) - 4):
                file = open(path, "w")
                file.write(str(content).replace("\'", "\""))
            else:
                file = open(path, "w")
                json.dump(content, file, indent=4)
            file.close()
        choose_format(content)
    else:
        def save_to_file_format(content):
            nonlocal decision
            filename = input("Enter file name\n")
            if filename == "":
                save_to_file_format(content)
            filename = filename.strip()
            if decision == "2":
                file = open("data/" + filename + ".txt", "w")
                file.write(str(content).replace("\'", "\""))
            else:
                file = open("data/" + filename + ".json", "w")
                json.dump(content, file, indent=4)
            file.close()
        save_to_file_format(content)
    sys.exit("\nFile saved! Bye!")
