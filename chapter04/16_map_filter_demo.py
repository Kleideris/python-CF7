cities = ["london", "paris", "barcelona", "athens", "Casablanka"]

# filter city names longer than 5 characters (using filster and lambda)
long_cities = filter(lambda city: len(city) > 5, cities)

# print(*long_cities, sep=", ")

cap_length_cities = list(map(lambda city: city.title(), long_cities))
print(*cap_length_cities, sep=", ")

# All in one...
clc = list(map(lambda city: city.title(), filter(lambda city: len(city) > 5, cities))) # is this efficient? i see 2 lambdas could it  be only one? TODO
print(*clc, sep=", ")

# list compr
cap_title_cities_compr = [city.title() for city in cities if len(city) > 5]
print(cap_title_cities_compr)



# print(f"Cities with names longer than 5 characters: {long_cities}") #why it doesnt work?? TODO
# print(*long_cities) #WHy this doent work? TODO