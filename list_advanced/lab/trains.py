number = int(input())
wagons = [0] * number
command = input()

while True:

    if command == "End":
        break
    split_command = command.split(" ")
    current_command = split_command[0]

    if current_command == "add":
        people_to_add = int(split_command[1])
        wagons[-1] += people_to_add
    elif current_command == "insert":
        index = int(split_command[1])
        people_to_insert = int(split_command[2])
        wagons[index] += people_to_insert
    elif current_command == "leave":
        index = int(split_command[1])
        people_to_leave = int(split_command[2])
        wagons[index] -= people_to_leave

    command = input()

print(wagons)
