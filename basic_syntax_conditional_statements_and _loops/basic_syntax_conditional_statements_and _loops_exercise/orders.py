n = int(input())
total = 0
for i in range(1, n + 1):
    price_capsul = float(input())
    day = int(input())
    needed_capsul = int(input())
    if 0.01 > price_capsul or price_capsul > 100 or day <= 0 or day > 31 or needed_capsul <= 0 or needed_capsul > 2000:
        continue
    else:
        price = price_capsul * day * needed_capsul
        total += price
        print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total:.2f}")



