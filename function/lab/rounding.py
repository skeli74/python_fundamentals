given_numbers = input().split()
final = []
given_numbers = list(map(float, given_numbers))
for num in given_numbers:
    final.append(round(num))
print(final)
