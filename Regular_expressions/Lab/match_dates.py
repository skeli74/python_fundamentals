import re

pattern = r"(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"

data = input()
dates = re.finditer(pattern, data)

for data in dates:
    d = data.groupdict()
    print(f"Day: {d['day']}, Month: {d['month']}, Year: {d['year']}")