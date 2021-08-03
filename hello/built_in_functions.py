metals = ["gold", "silver", "platinum", "palladium"]
print(list(filter(lambda metal:"p" in metal, metals)))
print(list(map(lambda val: val.replace("s","$"),metals)))
print(list(filter(lambda metal: len(metal) > 5, metals)))
print(list(map(lambda metal: metal*3, metals)))