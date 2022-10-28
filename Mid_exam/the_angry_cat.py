price_ratings = [int(el) for (el) in input().split(", ")]
entry_point_num = int(input())
item_types = input()

left_items = price_ratings[:entry_point_num]
right_items = price_ratings[entry_point_num + 1:]

sum_left_side = 0
sum_right_side = 0

if item_types == "expensive":
    for expensive_element in left_items:
        if expensive_element >= price_ratings[entry_point_num]:
            sum_left_side += expensive_element
    for expensive_element in right_items:
        if expensive_element >= price_ratings[entry_point_num]:
            sum_right_side += expensive_element
elif item_types == "cheap":
    for cheap_element in left_items:
        if cheap_element < price_ratings[entry_point_num]:
            sum_left_side += cheap_element
    for cheap_element in right_items:
        if cheap_element < price_ratings[entry_point_num]:
            sum_right_side += cheap_element

if sum_left_side < sum_right_side:
    print(f"Right - {sum_right_side}")
else:
    print(f"Left - {sum_left_side}")