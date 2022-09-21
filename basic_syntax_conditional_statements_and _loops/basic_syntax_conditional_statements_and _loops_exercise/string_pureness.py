n = int(input())
for i in range(1, n + 1):
    enter_str = input()
    flag = False
    for j in enter_str:
        if j == "," or j == "." or j == "_":
            flag = True
            break
    if flag:
        print(f"{enter_str} is not pure!")
    else:
        print(f"{enter_str} is pure.")


