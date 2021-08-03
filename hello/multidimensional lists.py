flavours = [
    ["honeydew","apple","strawberry",],
    ["cranberry","walnut","blueberry"],
    ["black currant","frost"]
]
# print(flavours)
# print(flavours[1])
# print(flavours[1][2])
# print(flavours[-1][-1])

new_flavours = []
for flavour in flavours:
    for few_flavours in flavour:
        new_flavours.append(few_flavours)
print(new_flavours)

print("a""b""c")