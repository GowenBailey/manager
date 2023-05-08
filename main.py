all_assignments = {}

def add(all_assignments):
    name = input("Name: ")
    points = int(input("Points: "))
    all_assignments[points] = name

def schedule(all_assignments):
    list_form = sorted(all_assignments.items(), key=lambda x:x[1])
    new_dict = dict(list_form)
    print(new_dict)

def main_screen(all_assignments):
    select_screen = input("Type 1 to add an assignment or 2 to see assignments: ")
    if select_screen == "1":
        add(all_assignments)
    elif select_screen == "2":
        schedule(all_assignments)

while True:
    main_screen(all_assignments)



    