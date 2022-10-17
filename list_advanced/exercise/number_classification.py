def positive(number):
    return [num for num in number if int(num) >= 0]


def negative(number):
    return [num for num in number if int(num) < 0]


def even(number):
    return [num for num in number if int(num) % 2 == 0]


def odd(number):
    return [num for num in number if int(num) % 2 != 0]


enter_numbers = input().split(", ")

print(f"Positive: {', '.join(positive(enter_numbers))}")
print(f"Negative: {', '.join(negative(enter_numbers))}")
print(f"Even: {', '.join(even(enter_numbers))}")
print(f"Odd: {', '.join(odd(enter_numbers))}")
