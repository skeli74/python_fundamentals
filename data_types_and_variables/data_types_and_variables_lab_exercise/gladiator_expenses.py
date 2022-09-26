lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
trashed_helmet = 0
trashed_sword = 0
trashed_shield = 0
trashed_armor = 0
trashed_shield_counter = 0
result = 0
for fights in range(1, lost_fights_count +1):
    if fights % 2 == 0:
        trashed_helmet += helmet_price
    if fights % 3 == 0:
        trashed_sword += sword_price
    if fights % 2 == 0 and fights % 3 == 0:
        trashed_shield += shield_price
        trashed_shield_counter += 1
        if trashed_shield_counter % 2 == 0:
            trashed_armor += armor_price
    total = trashed_helmet + trashed_sword + trashed_shield + trashed_armor
    result += total

print(f"Gladiator expenses: {total:.2f} aureus")
