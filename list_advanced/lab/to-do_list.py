notes = []

while True:
    command = input()

    if command == "End":
        break

    split_command = command.split("-")
    priority = int(split_command[0])
    note = split_command[1]
    notes.append([priority, note])

sorted_notes = []
for task in sorted(notes):
    sorted_notes.append(task[1])

print(sorted_notes)
