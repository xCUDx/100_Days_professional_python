foods = "sushi", "maggi", "coffee"
food =  ("sushi", "maggi", "coffee")
print(type(foods))
print(type(food))

birthday = 8, 1, 2002
print(birthday[-1])
print(birthday[0])
# birthday[1] = 13

cakes = (
    ["vanilla", "chocolate", "butterscotch"],
    ["Blackforest", "Hazelnutcream", "americannut"]
)
cakes[1][-1] = "pineapple"
print(cakes[1])

# Unpacking_of _a_tuple
employee = ("Steve", "Jobs", "CEO", "50")
# first_name = employee[0]
# last_name = employee[1]
# position = employee[3]
# age = employee[4]

# alternate
first_name, last_name, position, age = employee
print(first_name, last_name, position)

subject, verb, adjective = ("Python", "is", "tough")
print(subject, adjective)

#swaping
a = 10
b = 5
a, b = b, a
print(a)
print(b)

worker = ("Jeff", "Bezos", "CEO", "56")
name, name2, *details = worker
print(name)
print(details)

name, *details = worker
print(details)

def accept_stuff(*args):
    print(type(args))
    print(args)
accept_stuff(1)

# find the greatest among
def greatest_number(*numbers):
    my_max = numbers[0]
    for number in numbers:
        if number > my_max:
            my_max = number
    return my_max
print(greatest_number(1234, 33334, 777547, 866803.765))

# if 2nd arguments in tuples where new argument before asterisk(*)
def greatest_number(word, *numbers):
    print(word)
    my_max = word
    for number in numbers:
        if number > my_max:
            my_max = number
    return my_max
print(greatest_number(911234, 33334, 777547, 966803.765))

# if 2nd arguments in tuples where new argument after asterisk(*)
def greatest_number(*numbers, word):
    print(word)
    my_max = word
    for number in numbers:
        if number > my_max:
            my_max = number
    return my_max
print(greatest_number(911234, 33334, 777547, 966803.765))

