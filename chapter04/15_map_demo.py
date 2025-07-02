cities = ["london", "paris", "athens", "barceliona"]

cap_cities = list(map(lambda city: city.title(), cities))

print(f"Cap cities: {cap_cities}")

# TODO: na to skefte sto spiti
cap_cities2 = list(map(lambda city: city[0].upper(), cities))
print(f"Cap cities: {cap_cities2}")
#--------------------------------