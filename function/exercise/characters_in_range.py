def characters(a, b):
    list_of_characters = []
    result = None
    for simbol in range(ord(a) + 1, ord(b)):
        list_of_characters.append(chr(simbol))
    result = " ".join(list_of_characters)
    return result


first_characters = input()
second_characters = input()

print(characters(first_characters, second_characters))
