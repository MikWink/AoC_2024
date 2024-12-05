from utilities import read_file

def split_input(input):
    break_point = 0
    rules = []
    updates = []
    for i, line in enumerate(input):
        if line == "":
            break_point = i
            break
        rules += [line]

    for i in range(break_point + 1, len(input)):
        updates += [input[i]]
    return rules, updates

def check_needed_rules(rules, update):
    applied_rules = []
    pages = update.split(",")
    for page in pages:
        for rule in rules:
            if page == rule[:2]:
                applied_rules += [rule]
    return applied_rules

def check_single_page(index, pages, rules):
    return False

def check_conflict(applied_rules, update):
    pages = update.split(",")
    for i, page in enumerate(pages):
        rules_per_number =[]
        for rule in applied_rules:
            if page == rule[:2]:
                rules_per_number += [rule]
        if not check_single_page(i, pages, rules_per_number):
            break
    return True


input = read_file("input.txt")
rules, updates = split_input(input)
for update in updates:
    applied_rules = check_needed_rules(rules, update)
    print(f"\nUpdate:\n{update}")
    if(check_conflict(applied_rules, update)):
        print("Conflict")
    else:
        print("No Conflict")