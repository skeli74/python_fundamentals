the_number_of_snowballs = int(input())
highest_value = 0
weight = 0
time = 0
quality = 0
for snowballs in range(the_number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    result = (snowball_weight / snowball_time) ** snowball_quality
    if result > highest_value:
        highest_value = result
        weight = snowball_weight
        time = snowball_time
        quality = snowball_quality
print(f"{weight} : {time} = {int(highest_value)} ({quality})")
