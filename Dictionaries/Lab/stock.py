elements = input().split()
searched_items = input().split()
bakery = {}

for element in range(0, len(elements), 2):
    key = elements[element]
    value = elements[element + 1]
    bakery[key] = int(value)

for product in searched_items:
    if product in bakery.keys():
        quantity = bakery[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


