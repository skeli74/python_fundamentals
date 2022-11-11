strings = input().split()

result = ""

for words in strings:
    result += words * len(words)

print(result)