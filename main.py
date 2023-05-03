all_assignments = [

]

def add():
    assignment_info = []
    name = input("Name: ")
    assignment_info.append(name)
    days_until_due = int(input("Day's until due: "))
    assignment_info.append(days_until_due)
    points = int(input("Points: "))
    assignment_info.append(points)
    all_assignments.append(assignment_info)
    

def schedule():
    sorted(all_assignments, key=lambda assignment_info: assignment_info[2])
    print(all_assignments)

def main_screen():
    select_screen = input("Type 1 to add an assignment or 2 to see assignments: ")
    if select_screen == "1":
        add()
    elif select_screen == "2":
        schedule()

while True:
    main_screen()