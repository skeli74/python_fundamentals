def digits():
    list_of_enter = []
    for num in enter:
        list_of_enter.append(num)
    numbers_of_enter = list(map(int, list_of_enter))
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for n in numbers_of_enter:
        if n % 2 == 0:
            sum_of_even_digits += n
        else:
            sum_of_odd_digits += n
    return sum_of_odd_digits, sum_of_even_digits



enter = input()
result = digits()
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")
