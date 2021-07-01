# Create an empty list and assign it to the variable "empty".
empty = []

# Create a list with a single Boolean — True — and assign it to the variable "active".
active = [True]

# Create a list with 5 integers of your choice and assign it to the variable "favorite_numbers".
favorite_numbers = [4, 6, 11, 13, 29]

# Create a list with 3 strings  — "red", "green", "blue" — and assign it to the variable "colors".
colors = ["red", "green", "blue"]

# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise
def is_long(elements):
    return len(elements) > 5


# Define a first_and_last function that accepts a list of strings.
# The function should return a concatenation of the first element and the last element.
# Assume the list will always have 1 or more elements.
#
# first_and_last(["a", "b", "c"])        => "ac"
# first_and_last(["bob", "tom", "rob"])  => "bobrob"
# first_and_last(["a"])                  => "aa"
def first_and_last(string):
    return string[0] + string[-1]
string = "hello", "blue", "green"
print(first_and_last(string))

# Define a product_of_even_indices function that accepts a list of numbers.
# The list will always have 6 total elements.
# The function should return the product (multiplied total) of all numbers at an even index (0, 2, 4).
#
# product_of_even_indices([1, 2, 3, 4, 5, 6])    =>  15
# product_of_even_indices([3, 4, 3, 5, 3, 6])    =>  27
def product_of_even_indices(product):
    return product[0] * product[2] * product[4]
product = 1, 2, 4, 5, 6, 7
print(product_of_even_indices(product))


# Define a first_letter_of_last_string function that accepts a list of strings.
# It should return one character — the first letter of the last string in the list.
# Assume the list will always have at least one string.
#
# first_letter_of_last_string(["cat", "dog", "zebra"]) => "z"
# first_letter_of_last_string(["nonsense"]) => "n"
def first_letter_of_last_string(word):
    return word[-1][0]
word = "piano,huckelberry"
print(first_letter_of_last_string(word))

# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element to the end of the list.
# If the number is odd, return the list elements from index 0 (inclusive) to 2 (exclusive)
# EXAMPLE:
# values = ["a", "b", "c", "d", "e", "f"]
# split_in_two(values, 3)     => ["a", "b"]
# split_in_two(values, 4)     => ["c", "d", "e", "f"]
# split_in_two(values, 1)     => ["a", "b"]
# split_in_two(values, 10)    => ["c", "d", "e", "f"]

def split_in_two(list, a):
    if a % 2 == 0:
        return list[2:]
    else:
        return list[0:2]
list = []
print(split_in_two(list, 5))

# Declare a nested_extraction function that accepts a list of lists and an index position.
# The function should use the index as the basis of finding both the nested list
# and the element from that list with the given index position
# You can assume the number of lists will always be equal to
# the number of elements within each of them.
#
# nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
# nested_extraction(nl, 0)  => 3
# nested_extraction(nl, 1)  => 8
# nested_extraction(nl, 2)  => 12

def nested_extraction(a, b):
    return a[b][b]
nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
print(nested_extraction(nl,2))

# Declare a beginning_and_end function that accepts a list of elements.
# It should return True if the first and
# last elements in the list are equal and False if they are unequal.
# Assume the list will always have at least 1 element.
#
# beginning_and_end([1, 2, 3, 1])     => True
# beginning_and_end([1, 2, 3, 4, 5])  => False
# beginning_and_end(["a", "b", "a"])  => True
# beginning_and_end([15])             => True

def beginning_and_end(numbers):
    if numbers[0] == numbers[-1]:
        return True
    else:
        return False
numbers = [1, 2, 3, 4, 5, ]
print(beginning_and_end(numbers))

# Declare a long_word_in_collection function that accepts a list and a string.
# The function should return True if
#   - the string exists in the list AND
#   - the string has more than 4 characters.
#
# words = ["cat", "dog", "rhino"]
# long_word_in_collection(words, "rhino")  => True
# long_word_in_collection(words, "cat")    => False
# long_word_in_collection(words, "monkey") => False

def long_word_in_collection(c, d):
    if d in c and len(d) > 4:
        return True
    else:
        return False
values = ["cat", "dog", "rhino"]
print(long_word_in_collection(values, "rhino"))

free = ["hello", "gte", "hy", "hyr"]
print(free[6])






