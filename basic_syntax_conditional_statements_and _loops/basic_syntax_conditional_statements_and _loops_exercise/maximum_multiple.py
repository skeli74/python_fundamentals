enter = int(input())
border = int(input())
for i in range(1, border + 1):
    n = i
    if n % enter == 0:
        result = n
print(result)