# Declare a right_words function that accepts a list of words and a number.
# Return a new list with the words that have a length equal to the number.
# Do NOT use list comprehension.
#
# EXAMPLES:
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3)     => ['cat', 'dog', 'ace']
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5)     => ['heart']
# right_words([], 4)                                         => []

# def right_words(words,number):
#     return list(word for word in words if len(word) == number)
# print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))

# using_filter_an_lambda_function
def right_words(words,number):
    return list(filter(lambda word: len(word)== number, words))
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))

# Declare an only_odds function.
# It should accept a list of whole numbers.
# It should return a list with only the odd numbers from the original list.
# Do NOT use list comprehension.
#%
# EXAMPLES:
# only_odds([1, 3, 5, 6, 7, 8])      =>  [1, 3, 5, 7]
# only_odds([2, 4, 6, 8])            =>  []
def only_odds(numbers):
    return list(filter(lambda number: number%2 != 0, numbers))
print(only_odds([1, 3, 5, 6, 7, 8]))

# def only_odds(numbers):
#     return list(number for number in numbers if number%2 !=0)
print(only_odds([1, 3, 5, 6, 7, 8]))

# Declare a count_of_a function that accepts a list of strings.
# It should return a list with counts of how many “a” characters appear per string.
# Do NOT use list comprehension.
#
# EXAMPLES:
# count_of_a(["alligator", "aardvark", "albatross"])    => [2, 3, 2]
# count_of_a(["plywood"])                               => [0]
# count_of_a([])                                        => []
def count_of_function(words):
   return [word.count("a") for word in words]
print(count_of_function(["alligator", "aardvark", "albatross"]))

# def count_of_a(words):
#     return list(map(lambda word:word.count("a"), words))
# print(count_of_a(["alligator", "aardvark", "albatross"]))

number = 0.12345678
print(format(number, "f"))
