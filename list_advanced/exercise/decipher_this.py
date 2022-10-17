def decipher(character, switched):
    return chr(character) + switched


secret_message = input().split()
message = ""
final_message = []
ascii_code = []
secret_string = []


for decoding in secret_message:
    for character in decoding:
        if character.isdigit():
            ascii_code.append(character)
        elif character.isalpha():
            secret_string.append(character)
    secret_string[-1], secret_string[0] = secret_string[0], secret_string[-1]
    first_part = "".join(ascii_code)
    second_part = "".join(secret_string)
    message = (decipher(int(first_part), second_part))
    final_message.append(message)

    ascii_code = []
    secret_string = []

print(" ".join(final_message))
