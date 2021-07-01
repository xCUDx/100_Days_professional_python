# print("it is here")
#
# def fun_stuff():
#     a = 15
#     print("hello")
#     print("thank you")
#     a = 10
#     return a
#
# important = fun_stuff()c
# print(fun_stuff())

#define a number that iterates over each number
#multiply each number with one less than its index position
#and return total sum of those products
#sample case
# 1 * -1 = -1
# 2 * 0 = 0

def number_over_number(numbers):
    total = 0
    for index,number in enumerate(numbers):
        total = total + number*(index-1)
    return total
print(number_over_number([1,2,3,4,5]))