enter = input()

vowels = ['a', 'o', 'u', 'e', 'i']

output = ""

for char in enter:
    if char.lower() not in vowels:
        output += char

print(output)
