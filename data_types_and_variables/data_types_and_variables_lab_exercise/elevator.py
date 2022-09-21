import math
num_of_people = int(input())
capacity = int(input())
curses = math.ceil(num_of_people / capacity)
print(curses)
