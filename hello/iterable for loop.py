#for strings
# dinner = "steak and potatoes"
# for dish in dinner:
#     print(dish)

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     print(number * number)
#
# novelists = ["Fitzgerald", "Hemingway", "steinbeck"]
# for novelist in novelists:
#     print(len(novelists))
#
# total = 0
# for number in numbers:
#     total = total + number
#     print(total)

#addition for odd numbers
# values = [3, 6, 9, 12, 15, 18, 21, 24]
# other_values = [5, 10, 15, 20, 25, 30]
#
# def odd_sum(numbers):
#     total = 0
#     for number in numbers:
#         if number % 2 == 1:
#             total = total + number
#     return  (total)
#
#
# print(odd_sum(values))


# greatest_number
def greatest_number(numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

set = [1, 2, 3, 4, 5, 6]
print(greatest_number(set))
