quantity_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
guineas_weight = float(input()) * 1000

for day in range(1, 30 + 1):
    if quantity_food <= 0 or quantity_hay <= 0 or quantity_cover <= 0:
        break
    quantity_food -= 300
    if day % 2 == 0:
        quantity_hay -= quantity_food * 0.05

    if day % 3 == 0:
        quantity_cover -= guineas_weight / 3

if quantity_food > 0 and quantity_hay > 0 and quantity_cover > 0:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food / 1000:.2f}, Hay: {quantity_hay / 1000:.2f}"
          f", Cover: {quantity_cover / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")
