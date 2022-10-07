def sum_numbers(a, b, c):
    add = a + b
    result = add - c
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(sum_numbers(first_num, second_num, third_num))
