errands = ["gym", "lunch", "work", "sleep"]
print(enumerate(errands))
for index,errands in enumerate(errands,):
    print(f"{errands} is the # {index} for the day")

for index,errands in enumerate(errands, 1):
    print(f"{errands} is the # {index} for the day")