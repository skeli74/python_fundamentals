count_chars_in_a_string = {}
enter = input()
chars = ""
for char in enter:
    if char == " ":
        continue
    chars += char
for symbol in chars:
    if symbol not in count_chars_in_a_string.keys():
        count_chars_in_a_string[symbol] = 0
    count_chars_in_a_string[symbol] += 1
for char, occurrences in count_chars_in_a_string.items():
    print(f"{char} -> {occurrences}")
