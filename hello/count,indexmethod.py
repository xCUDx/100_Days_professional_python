#the count method
car_lot = ["ford","toyota","ford","leon","dodge","ford"]
print(car_lot.count("ferrari"))
print(car_lot.count("ford"))

hours_of_sleep = ["7.0", "7.2", "3.5", "6.5", "7.0", "9.0", "7.0"]
print(hours_of_sleep.count("7.0"))
print(hours_of_sleep.count("7"))

#the index method
pizzas = ["mushroom", "pepperoni", "sausage", "barbecue chicken", "pepperoni", "sausage"]
print(pizzas.index("pepperoni"))
print(pizzas.index("pepperoni", 2))
if "olives" in pizzas:
    print(pizzas.index("olives"))
else:
    print(pizzas.index("sausage", 3))