#list comprehension
numbers = [3,4,5,6,7]
# squares = []
# for number in numbers:
#     squares.append(number**2)
# print(squares)

# alternate
squares = [number ** 2 for number in numbers]
print(squares)

rivers = ["ganga", "yamuna", "brahamaputra"]
print([len(river) for river in rivers])

expressions = ["lol", "rofl", "lmao"]
print([expression.upper() for expression in expressions])

decimals = [4.95, 3.39, 1.08]
print([int(decimal) for decimal in decimals])

print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "donut"])

print([number / 2 for number in range(20)])

cars = [
    "Ford Mustang",
    "Ford F150",
    "Ford Denali",
    "Ford Explorer",
    "Toyota Harrier",
    "Volkswagen Tiguan",
    "Volkswagen Arteon"
]
# Ford_cars = []
# for car in cars:
#     if "Ford" in car:
#         Ford_cars.append(car)
# print(Ford_cars)

Ford_cars = [car for car in cars if "Ford" in car]
print(Ford_cars)

print([len(car) for car in cars if "Volkswagen" in car])

print([car.index("") for car in cars if "Volkswagen" in car])

print([car.split()[1] for car in cars if "Ford" in car])