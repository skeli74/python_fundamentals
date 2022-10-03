def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [ i for i in num_list if i != 0]
    x.extend(a)
    return(x)
enter = input()

convert_list = enter.split(",")
convert_list = list(map(int, convert_list))
zero_end = move_zero(convert_list)

print(zero_end)

