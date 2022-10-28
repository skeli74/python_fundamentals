enter = input()
player_one = 0
player_two = 0
player_one += enter.count("1")
player_two += enter.count("2")
for i in range(2):
    enter = input()
    player_one += enter.count("1")
    player_two += enter.count("2")
if player_one > player_two:
    print("First player won")
elif player_two > player_one:
    print("Second player won")
else:
    print("Draw!")
enter = input().split()
player_one = 0
player_two = 0
player_one += enter.count("1")
player_two += enter.count("2")
for i in range(2):
    enter = input().split()
    player_one += enter.count("1")
    player_two += enter.count("2")
if player_one > player_two:
    print("First player won")
elif player_two > player_one:
    print("Second player won")
else:
    print("Draw!")
