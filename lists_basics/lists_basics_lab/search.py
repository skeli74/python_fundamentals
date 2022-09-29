n = int(input())
word = input()
strings = []
for i in range(n):
    enter = input()
    strings.append(enter)
print(strings)
for i in range(len(strings) - 1, -1, -1):
    element = strings[i]
    if word not in element:
        strings.remove(element)
print(strings)
