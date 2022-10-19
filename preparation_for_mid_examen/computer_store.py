command = input()

flag = False
prise = 0
total_price = 0

while True:
    if command == "special" or command == "regular":
        flag = True
        break

    current_command = float(command)

    if current_command < 0:
        print("Invalid price!")
        command = input()
        continue
    else:
        prise += current_command
    command = input()
taxes = prise * 0.20
total_price = prise + taxes
if command == "special":
    total_price -= total_price * 0.10
if total_price <= 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {prise:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
