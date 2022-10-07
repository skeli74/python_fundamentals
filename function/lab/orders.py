def order(stok, count):
    total = None
    if stok == "coffee":
        total = count * 1.50
    elif stok == "water":
        total = count * 1.00
    elif stok == "coke":
        total = count * 1.40
    elif stok == "snacks":
        total = count * 2.00
    return total


product = input()
count_of_product = int(input())
print(f"{order(product, count_of_product):.2f}")
