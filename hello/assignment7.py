# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string “even”.
# If the integer is odd, the function should return the string “odd”.
#
# even_or_odd(2)    => "even"
# even_or_odd(0)    => "even"
# even_or_odd(13)   => "odd"
# even_or_odd(9)    => "odd"
def even_or_odd(number):
    if number % 2 == 0:
        return("even")
    return ("odd")
print(even_or_odd(36))

# Define a truthy_or_falsy function that accepts a single argument.
# The function should return a string that reads "The value _____ is ______"
# where the first space is the argument and the second space
# is either 'truthy' or 'falsy'. See the sample invocations below.
#
# truthy_or_falsy(0)        => "The value 0 is falsy"
# truthy_or_falsy(5)        => "The value 5 is truthy"
# truthy_or_falsy("Hello")  => "The value Hello is truthy"
# truthy_or_falsy("")       => "The value  is falsy"
def truthy_or_falsy(value):
    if bool(value):
        return f"the value {value} is truthy "
    return f"the value {value} is falsy"
print(truthy_or_falsy(78))

# Declare a negative_energy function that accepts a numeric argument and returns its absolute value.
# The absolute value is the number's distance from zero.
#
# negative_energy(5)    => 5
# negative_energy(10)   => 10
# negative_energy(-5)   => 5
# negative_energy(-8)   => 8
# negative_energy(0)    => 0

# def negative_energy(a):
#     if a < 0:
#         return abs(a)
#     elif a > 0:
#         return abs(a)
#     elif a == 0:
#         return 0
#     else:
#         return "end of my thinking capacity"
# print(negative_energy(-0))

#alternate
def negative_energy(b):
    if b >= 0:
        return b
    elif b < 0:
        return -1 * b
print(negative_energy(-0))

# Define a divisible_by_three_and_four function that accepts a number as its argument.
# It should return True if the number is evenly divisible by both 3 and 4 .
# It should return False otherwise.
#
# divisible_by_three_and_four(3)   => False
# divisible_by_three_and_four(4)   => False
# divisible_by_three_and_four(12)  => True
# divisible_by_three_and_four(18)  => False
# divisible_by_three_and_four(24)  => True

def divisible_by_three_and_four(x):
    if x % 3 == 0 and x % 4 == 0:
        return "true"
    else:
        return "false"
print(divisible_by_three_and_four(3))

# Declare a string_theory function that accepts a string as an argument.
# It should return True if the string has more than 3 characters
# and starts with a capital “S”. It should return False otherwise.
#
# string_theory("Sansa") => True
# string_theory("Story") => True
# string_theory("See") => False
# string_theory("Fable") => False
def string_theory(word):
    if len(word) > 3 and word[0] == "S":
        return "true"
    else:
        return("false")

print(string_theory("Seoul"))

# Define a function called "factorial" that accepts a single number as input
#
# A factorial represents the product of all numbers up to, and including, that number.
# For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120
#
# Return the factorial calculation from your function. You should NOT use any kind of loops.
# Instead, utilize recursion. Your function MUST call itself.
# See sample inputs and return values below
#
# factorial(1) => 1
# factorial(2) => 2
# factorial(3) => 6
# factorial(4) => 24
# factorial(5) => 120

# def factorial(num):
#     if num <= 0:
#         return 1
#     return num * factorial(num - 1)
# print(factorial(1))

def factoraial(num):
    value = num
    if value <= 0:
        return 1
    while value >= 1:
        print(value)
        num -= 1
        value = value * (num)




print(factoraial(6))





