initial_list = input().split("!")
command = input()
while command != "Go Shopping!":
    action = command.split(" ")
    if action[0] == "Urgent":
        if action[1] in initial_list:
            command = input()
            continue
        else:
            initial_list.insert(0, action[1])
            command = input()
    elif action[0] == "Unnecessary":
        if action[1] not in initial_list:
            command = input()
            continue
        else:
            initial_list.remove(action[1])
            command = input()
    elif action[0] == "Correct":
        if action[1] in initial_list:
            initial_list = list(map(lambda x: x.replace(action[1], action[2]), initial_list))
            command = input()
        else:
            command = input()
            continue
    elif action[0] == "Rearrange":
        if action[1] in initial_list:
            initial_list.remove(action[1])
            initial_list.append(action[1])
            command = input()
        else:
            command = input()
            continue


print(", ".join(initial_list))
