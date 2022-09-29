n = int(input())
positive = []
negative = []
for i in range(n):
    enter = int(input())
    if enter >= 0:
        positive.append(enter)
    else:
        negative.append(enter)
print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")
