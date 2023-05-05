all_assignments = {}

def add(all_assignments):
    name = input("Name: ")
    points = int(input("Points: "))
    all_assignments[points] = name

def schedule(all_assignments):
    sorted(all_assignments.items(), key=lambda item: item[1])
    print(all_assignments)

def main_screen(all_assignments):
    select_screen = input("Type 1 to add an assignment or 2 to see assignments: ")
    if select_screen == "1":
        add(all_assignments)
    elif select_screen == "2":
        schedule(all_assignments)

while True:
    main_screen(all_assignments)