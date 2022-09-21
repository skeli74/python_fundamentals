number_of_lines = int(input())
result = 0
for n in range(number_of_lines):
    letter_per_line = ord(input())
    result += letter_per_line
print(f"The sum equals: {result}")

