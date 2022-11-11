text = input()
digits = []
letters = []
other = []

for characters in text:
    if characters.isdigit():
        digits.append(characters)
    elif characters.isalpha():
        letters.append(characters)
    else:
        other.append(characters)
print("".join(digits))
print("".join(letters))
print("".join(other))