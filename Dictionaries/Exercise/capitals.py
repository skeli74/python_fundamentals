country_names = input().split(", ")
city_names = input().split(", ")
result = dict(zip(country_names, city_names))

for country, capital in result.items():
    print(f"{country} -> {capital}")

