number_of_lines = int(input())
add_liters = 0
for i in range(number_of_lines):
    liters_of_water = int(input())
    if liters_of_water + add_liters > 255:
        print("Insufficient capacity!")
        continue
    else:
        add_liters += liters_of_water
print(add_liters)
