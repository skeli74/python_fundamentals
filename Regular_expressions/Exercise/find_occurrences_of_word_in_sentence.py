import re

sentences = input()
word = input()
pattern = fr"\b{word}\b"
matches = re.findall(pattern, sentences, flags=re.IGNORECASE )

print(len(matches))

