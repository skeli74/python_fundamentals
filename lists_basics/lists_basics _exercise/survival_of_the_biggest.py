list_of_numbers = input().split()
count_of_numbers_to_remove = int(input())
list_of_numbers = list(map(int, list_of_numbers))
for number in range(count_of_numbers_to_remove):
    list_of_numbers.remove(min(list_of_numbers))
list_of_numbers = list(map(str, list_of_numbers))
result = ", ".join(list_of_numbers)
print(result)