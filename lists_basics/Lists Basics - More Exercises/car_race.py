sequence_of_numbers = list(map(int, input().split()))
middle_index = len(sequence_of_numbers) // 2
time_left = 0
time_right = 0
for left in sequence_of_numbers[0:middle_index]:
    if left == 0:
        time_left = time_left * 0.80
    else:
        time_left += left
for right in sequence_of_numbers[len(sequence_of_numbers):middle_index:-1]:
    if right == 0:
        time_right = time_right * 0.80
    else:
        time_right += right
if time_left < time_right:
    print(f"The winner is left with total time: {time_left:.1f}")
else:
    print(f"The winner is right with total time: {time_right:.1f}")