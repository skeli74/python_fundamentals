given_numbers = input().split()
final = []
given_numbers = list(map(int, given_numbers))
for num in given_numbers:
    if num % 2 == 0:
        final.append(num)
print(final)