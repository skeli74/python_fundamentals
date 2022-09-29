num = abs(int(input()))
length = abs(int(input()))
my_list = []
for i in range(num, 10000000 +1):
    if i % num == 0:
        my_list.append(i)
        if len(my_list) >= length:
            break
print(my_list)
