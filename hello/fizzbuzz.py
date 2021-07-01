# FizzBuzz is a popular programming problem to test a developer's ability to think logically
# with code.
# The problem is simple but deceptive.
# Define a fizzbuzz function that accepts a single number as an argument.
# The function should print every number from 1 to that argument.

# There are a couple caveats.
# If the number is divisible by 3, print "Fizz" instead of the number.
# If the number is divisible by 5, print "Buzz" instead of the number.
# If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.
# If the number is not divisible by either 3 or 5, just print the number.

# Example: fizzbuzz(30)should print:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# def fizz_buzz(value):
#     count = 1
#     while count <= value:
#         if count % 15 == 0:
#           print("fizzbuzz")
#         elif count % 5 == 0:
#           print("buzz")
#         elif count % 3 == 0:
#           print("fizz")
#         else:
#           print(count)
#         count += 1
#
# print(fizz_buzz(30))#

# recursive approach

def fizzbuzz(final_number):
    current_number = 1
    while current_number <= final_number:
        if current_number % 15 == 0:
          print("FizzBuzz")
        elif current_number % 3 == 0:
          print("Fizz")
        elif current_number % 5 == 0:
          print("Buzz")
        else:
          print(current_number)
        current_number += 1


print(fizzbuzz(20))
#


