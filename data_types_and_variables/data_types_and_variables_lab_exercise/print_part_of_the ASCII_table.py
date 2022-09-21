start = int(input())
stop = int(input())
my_list = []
for i in range(start, stop + 1):
    symbol = chr(i)
    my_list.append(symbol)
print(*my_list)
