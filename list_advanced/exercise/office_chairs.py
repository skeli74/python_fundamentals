number_of_rooms = int(input())
chairs = 0
visitors = 0

for n in range(1, number_of_rooms + 1):
    chairs_visitors = input().split()
    chairs += len(chairs_visitors[0])
    visitors += int(chairs_visitors[1])
    if len(chairs_visitors[0]) < int(chairs_visitors[1]):
        print(f"{int(chairs_visitors[1]) - len(chairs_visitors[0])} more chairs needed in room {n}")

if chairs >= visitors:
    print(f"Game On, {chairs - visitors} free chairs left")
