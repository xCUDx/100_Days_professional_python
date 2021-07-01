# without continue keyword
# def sum_of_positive_number(numbers):
#     total = 0
#     for number in numbers:
#         if number > 0:
#             total += number
#     return total
# print(sum_of_positive_number([1,2,-3,4,-5]))

def sum_of_positive_numbers(numbers):
    total = 0
    for number in numbers:
        if number < 0:
            continue
        total += number
    return  total
print(sum_of_positive_numbers([1,2,-3,4,-5]))
