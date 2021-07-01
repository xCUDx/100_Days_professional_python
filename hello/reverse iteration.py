# reversed iteration function
# without reverse function
the_simpsons = ["homer","marge","lisa","maggie"]
for character in  the_simpsons[::-1]:
    print(f"{character} has total of{len(character)} characters")

print(reversed(the_simpsons))
print(type(the_simpsons))

for character in reversed(the_simpsons):
    print(f"{character} has a total of {len(character)} characters")