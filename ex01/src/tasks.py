import todolistv2


def find_task(content):
    text = input("Type keyword for search!\n")
    if text == "":
        find_task(content)
    print("|----------|--------|---------------------------------------------------------------------------|")
    print("| PRIORITY | STATUS |                                   TASK                                    |")
    print("|----------|--------|---------------------------------------------------------------------------|")
    for note in content["NOTES"]:
        if str(note["PRIORITY"]).find(text) != -1 or str(note["STATUS"]).find(text) != -1 or str(note["TASK"]).find(text) != -1:
            print(
                f"|   {note["PRIORITY"]}    |  {note["STATUS"]}   | {note["TASK"]}                           ")
            print("|----------|--------|---------------------------------------------------------------------------|")


def add_task(content):
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
    rez = list(content["NOTES"])
    rez.append({'PRIORITY': priority, 'STATUS': status, 'TASK': task})
    content["NOTES"] = rez


def print_tasks(content):
    print("|----------|--------|---------------------------------------------------------------------------|")
    print("| PRIORITY | STATUS |                                   TASK                                    |")
    print("|----------|--------|---------------------------------------------------------------------------|")
    for note in content["NOTES"]:
        print(
            f"|   {note["PRIORITY"]}    |  {note["STATUS"]}   | {note["TASK"]}                           ")
        print("|----------|--------|---------------------------------------------------------------------------|")
