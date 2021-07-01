# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#
# EXAMPLES
# sum_of_lengths(["Hello", "Bob"])                  => 8
# sum_of_lengths(["Nonsense"])                      => 8
# sum_of_lengths(["Nonsense", "or", "confidence"])  => 20

# code
# def sum_of_lengths(strings):
#     sub = 0
#     for string in strings:
#         sub = len(string) + sub
#     print (sub)
#
# novelists = ["Fitzgerald", "Hemingway", "steinbeck"]
# print(sum_of_lengths(novelists))


# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
# EXAMPLES
# product([1, 2, 3])     => 6
# product([4, 5, 6, 7])  => 840
# product([10])          => 10

# code
# def product_function(numbers):
#     product = 1
#     for number in numbers:
#      product = product * number
#     return (product)

# print(product_function([1, 3, 5]))


# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.
#
# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3

# code
def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

print(smallest_number([-3, -2, -1]))

# Define a concatenate function that accepts a list of strings.
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.
#
# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""

# code
def concatenate_function(strings):
    char = ""
    for string in strings:
        if len(string) > 2:
            char = char + string
    print(char)


strin = ["abc", "de", "ghi"]
print(concatenate_function(strin))

# Define a super_sum function that accepts a list of strings.
# The function should sum the index positions of the first occurence of the letter “s” in each word.
#
# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.
#
# super_sum([])                                 => 0
# super_sum(["mustache"])                       => 2
# super_sum(["mustache", "greatest"])           => 8
# super_sum(["mustache", "pessimist"])          => 4
# super_sum(["mustache", "greatest", "almost"]) => 12
def super_sum(strings):
    total = 0

    for string in strings:
        if "s" in string:
            index = string.index("s")
            total += index
    return total
print(super_sum(["mustache", "greatest", "almost"]))



