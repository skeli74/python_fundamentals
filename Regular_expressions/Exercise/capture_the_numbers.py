import re

lines = input()
pattern = r"\d+"

while lines:
    matches = re.findall(pattern, lines)
    if matches:
        print(" ".join(matches), end=" ")
    lines = input()

