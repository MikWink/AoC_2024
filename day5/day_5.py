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
                for sec_page in pages:
                    if sec_page == rule[3:]:
                        applied_rules += [rule]

    return applied_rules

def check_single_page(index, pages, rules):
    for rule in rules:
        for i, page in enumerate(pages):
            rule_number = rule[3:]
            if rule[3:] == page and i < index:
                return False

    return True

def check_conflict(applied_rules, update):
    pages = update.split(",")
    for i, page in enumerate(pages):
        rules_per_number =[]
        for rule in applied_rules:
            if page == rule[:2]:
                rules_per_number += [rule]
        if not check_single_page(i, pages, rules_per_number):
            return False
    return True


input = read_file("input.txt")
sum = 0
rules, updates = split_input(input)
for i, update in enumerate(updates):
    applied_rules = check_needed_rules(rules, update)
    print(f"\nUpdate:\n{update}\nRules: {applied_rules}")
    if(check_conflict(applied_rules, update)):
        ups = update.split(",")
        print(f"No Conflict:\nsum = {sum} + {ups[int(len(ups)/2)]} = {sum + int(ups[int(len(ups)/2)])}")
        sum += int(ups[int(len(ups)/2)])
    else:
        print("Conflict")

print("\nResult: ", sum)