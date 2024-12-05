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
    global used_rules
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

def fixd_update(update, applied_rules):
    up = update.split(",")
    for rule in applied_rules:
        position_first = up.index(rule[:2])
        position_sec = up.index(rule[3:])
        if position_first > position_sec:
            tmp = up[position_first]
            up[position_first] = up[position_sec]
            up[position_sec] = tmp
    return up

from collections import defaultdict, deque

def fix_update(update, applied_rules):
    pages = update.split(",")
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build the dependency graph
    for rule in applied_rules:
        src, dest = rule[:2], rule[3:]
        graph[src].append(dest)
        in_degree[dest] += 1
        if src not in in_degree:
            in_degree[src] = 0

    # Perform topological sorting
    queue = deque([page for page in pages if in_degree[page] == 0])
    sorted_pages = []

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Append any leftover pages that are not part of the rules
    unsorted_pages = [page for page in pages if page not in sorted_pages]
    sorted_pages.extend(unsorted_pages)

    return sorted_pages


input = read_file("input.txt")
sum = 0
sum_part2 = 0
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
        fixed_update = fix_update(update, applied_rules)
        print("Fixed Update: ", fixed_update)
        print(f"sum = {sum_part2} + {fixed_update[int(len(fixed_update) / 2)]} = {sum + int(fixed_update[int(len(fixed_update) / 2)])}")
        sum_part2 += int(fixed_update[int(len(fixed_update) / 2)])

print("\nResult Part 1: ", sum)
print("\nResult Part 2: ", sum_part2)