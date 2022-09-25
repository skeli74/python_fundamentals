group_size = int(input())
days_of_the_adventure = int(input())
coins = 0
companions = 0
companions += group_size
for days in range(1, days_of_the_adventure + 1):
    if days % 10 == 0:
        companions -= 2
    if days % 15 == 0:
        companions += 5
    if days % 3 == 0:
        coins -= companions * 3
    if days % 5 == 0:
        coins += 20 * companions
        if days % 3 == 0:
            coins -= companions * 2
    coins += 50
    coins -= companions * 2
result = int(coins / companions)
print(f"{companions} companions received {result} coins each.")
