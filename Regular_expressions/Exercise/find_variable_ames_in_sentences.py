import re

sentences = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
matches_names = re.findall(pattern, sentences)

if matches_names:
    print(",".join(matches_names))