enter = input()
j = ""
while enter != "End":
    if enter == "SoftUni":
        continue
    for i in enter:
        j += i * 2
    print(j)
    j = ""
    enter = input()