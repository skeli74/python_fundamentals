def data_type(first, second):
    if first == "int":
        result = int(second) * 2
        return result
    if first == "real":
        result = float(second) * 1.5
        return f"{result:.2f}"
    if first == "string":
        return f"${second}$"


first_command = input()
second_command = input()

print(data_type(first_command, second_command))
