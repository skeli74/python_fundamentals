number = float(input())
if number == 0:
    print("zero")
elif 0 < number < 1:
    print("small positive")
elif number > 1000000:
    print("large positive")
elif number >= 1:
    print("positive")
elif 0 > number > -1:
    print("small negative")
elif number < -1000000:
    print("large negative")
elif number <= 1:
    print("negative")

