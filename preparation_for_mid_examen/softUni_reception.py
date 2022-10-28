first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
threed_employee_efficiency = int(input())
count_of_students = int(input())

total_efficiency = first_employee_efficiency + second_employee_efficiency + threed_employee_efficiency
counter_hours = 0

while count_of_students > 0:
    count_of_students = count_of_students - total_efficiency
    counter_hours += 1
    if counter_hours % 4 == 0:
        counter_hours += 1


print(f"Time needed: {counter_hours}h.")





