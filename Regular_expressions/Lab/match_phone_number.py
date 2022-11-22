import re

pattern = r"\+\d[3-9]+(\s|-)2(\1)\d{3}(\1)\d{4}\b"

text = input()

matches = re.finditer(pattern, text)
matches = [p.group(0) for p in matches]

print(", ".join(matches))
