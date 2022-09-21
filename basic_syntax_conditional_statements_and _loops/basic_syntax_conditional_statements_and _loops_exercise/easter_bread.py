budget = float(input())
price_for_1_kg_flour = float(input())
price_for_1_pack_of_eggs = price_for_1_kg_flour * 0.75
price_for_1L_milk = price_for_1_kg_flour * 1.25
price_for_one_loaf = price_for_1L_milk * 0.25 + price_for_1_kg_flour + price_for_1_pack_of_eggs
loaf_of_bread = 0
colored_eggs = 0
while budget > price_for_one_loaf:
    loaf_of_bread += 1
    colored_eggs += 3
    budget -= price_for_one_loaf
    if loaf_of_bread % 3 == 0:
        missing_colored_eggs = loaf_of_bread - 2
        colored_eggs -= missing_colored_eggs
print(f"You made {loaf_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
