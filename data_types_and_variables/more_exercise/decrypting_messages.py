key = int(input())
number_of_lines = int(input())
decrypted_message = ""
for lines in range(number_of_lines):
    letter_per_line = (input())
    first_letter = ord(letter_per_line)
    decrypting = first_letter + key
    decrypting_letter = chr(decrypting)
    decrypted_message += decrypting_letter
print(decrypted_message)
