command = input()
coffee_counter = 0
while command != "END":
    if coffee_counter > 5:
        break
    if command != "coding" and command != "CODING" and command != "dog" and command != "cat" and\
            command != "DOG" and command != "CAT" and command != "movie" and command != "MOVIE":
        command = input()
        continue
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee_counter += 1
    else:
        coffee_counter += 2

    command = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)

