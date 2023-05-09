all_assignments = {}
list_form = []

def add(all_assignments):
    name = input("Name: ")
    points = int(input("Points: "))
    all_assignments[points] = name

def schedule(all_assignments, list_form):
    print("Here are your assignments organized by points: ")
    list_form = sorted(all_assignments.items(), key=lambda x:x[0], reverse=True)
    for index in range(len(list_form)):
        print(list_form[index])

def main_screen(all_assignments, list_form):
    select_screen = input("Type 1 to add an assignment or 2 to see assignments: ")
    if select_screen == "1":
        add(all_assignments)
    elif select_screen == "2":
        schedule(all_assignments, list_form)
    elif select_screen == "3":
        remove_assignment(list_form, all_assignments)

def remove_assignment(list_form, all_assignments):
    print("Choose an Assignment to Remove: ")
    for index in range(len(list_form)):
        print(list_form(index))
    removed_list = input("Type by name: ")
    for removed_list in list_form:
        list_form.remove(removed_list)


while True:
    main_screen(all_assignments, list_form)