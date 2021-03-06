# Define an only_evens function that accepts a list of numbers.
# It should return a new list consisting of only the even numbers from the original list.
#
# EXAMPLES
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5])              => []
# only_evens([])                     => []
def only_evens(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result
print(only_evens([1, 3, 5]))

# Define a long_strings function that accepts a list of strings.
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# EXAMPLES
# long_strings(["Hello", "Goodbye", "Sam"])  => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"])        => []
# long_strings([])                           => []
def long_strings(values):
    result = []
    for value in values:
        if len(value) >= 5:
            result.append(value)
    return result
print(long_strings(["Hello", "Goodbye", "Sam"]))