powerball_numbers = [4,8,15,16,23,42]
# def squares(numbers):
#     squares = []
#     for number in numbers:
#         squares.append(number**2)
#     return squares
# print(squares(powerball_numbers))

# def convert_to_float(numbers):
#     result = []
#     for number in numbers:
#         result.append(float(number))
#     return (result)
# print(convert_to_float(powerball_numbers))

def even_or_odd(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(True)
        elif number % 2 != 0:
            result.append(False)
    return result
print(even_or_odd(powerball_numbers))