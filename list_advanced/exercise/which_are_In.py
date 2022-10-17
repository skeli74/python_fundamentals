first_sequences = input().split(", ")
second_string = input().split(", ")
sub_string = []

for first_word in first_sequences:
    for second_word in second_string:
        if first_word in second_word:
            sub_string.append(first_word)
            break

print(sub_string)



