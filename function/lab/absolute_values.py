sequence_of_numbers = input().split()
final = []
sequence_of_numbers = list(map(float, sequence_of_numbers))
for num in sequence_of_numbers:
    final.append(abs(num))

print(final)
