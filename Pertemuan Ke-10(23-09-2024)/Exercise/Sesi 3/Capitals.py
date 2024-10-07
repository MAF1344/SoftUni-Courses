dict1 = input().split(", ")
dict2 = input().split(", ")

country_capital_dict = {country: capital_city for (country, capital_city) in zip(dict1, dict2)}

for (country, capital_city) in country_capital_dict.items():
    print(f"{country} -> {capital_city}")