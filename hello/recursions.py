# by using while loop
# def count_down_from(number):
#     value = number
#     while value > 0:
#         print(value)
#         value -= 1
# print(count_down_from(100))

#by using recursions
# def count_down_from(number):
#     if number <= 0:
#         return
#     print(number)
#     count_down_from(number - 1)
#
# print(count_down_from(10))


# printing a string from backwards to forward
# def reverse_string(word):
#     first_index = 0
#     last_index = len(word) - 1
#     new_word = ""
#     while last_index >= first_index:
#         new_word = new_word + str(last_index)    # new_word = new_word + str(last_index)
#         last_index -= 1
#         return new_word
#
# print(reverse_string("hello"))

# def reverse(str):
#     start_index = 0
#     last_index = len(str) - 1 # -1
#     reversed_string = "" # warts
#     while last_index >= start_index:
#         reversed_string += str[last_index]
#         last_index -= 1
#         return reversed_string
#
# print(reverse(""))

def reverse_string(str):
    if len(str) <= 0:
        return str
    return str[-1] + reverse_string(str[:-1])
print(reverse_string("betrio"))





