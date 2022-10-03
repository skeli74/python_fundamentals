gifts = input().split()
command = input()
while command != "No Money":
    command = command.split()
    operation, current_gift = command[0], command[1]
    if operation == f"OutOfStock":
        gifts = [None if gift == current_gift else gift for gift in gifts]
    elif operation == f"Required":
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = current_gift
    elif operation == f"JustInCase":
        gifts[-1] = current_gift
    command = input()
for gift in gifts:
    if gift is not None:
        print(f"{gift}", end=" ")
