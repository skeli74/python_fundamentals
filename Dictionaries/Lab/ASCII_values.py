list_of_char = input().split(", ")
characters = {key: ord(key) for key in list_of_char}
print(characters)