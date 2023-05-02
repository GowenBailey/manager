assignments_list = []

def add():
    name = input("Name: ")
    assignments_list.append(name)

def schedule():
    print(assignments_list)

def main_screen():
    select_screen = input("Type 1 to add an assignment or 2 to see assignments: ")
    if select_screen == "1":
        add()
    elif select_screen == "2":
        schedule()

while True:
    main_screen()