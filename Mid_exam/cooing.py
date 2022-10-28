import math

budget = float(input())
students = int(input())
price_for_package_of_flour = float(input())
price_for_single_egg = float(input())
price_for_single_apron = float(input())

needed_apron = math.floor(students * 0.20)


budget_for_one = price_for_package_of_flour + (price_for_single_egg * 10)

needed_money = (needed_apron * price_for_single_apron) + budget_for_one

for student in range(1, students + 1):
    if student % 5 == 0:
        needed_money -= price_for_package_of_flour

print(needed_money)





