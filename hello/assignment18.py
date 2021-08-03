# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# EXAMPLES
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0
def nested_sum(list1):
    sum = 0
    for elements in list1:
        for element in elements:
            sum += element
    return sum

print(nested_sum([[1, 2, 3], [4, 5]]))
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))

# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])    => ""

#  code
# def fancy_concatenate(lists):
#     new_list = []
#     for values in lists:
#         for value in values:
#             if len(values) == 3:
#                 new_list += value
#     return ("".join(new_list))
# print(fancy_concatenate([["A", "B", "C"]]))
# print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]))

#alternate
def fancy_concatenate(lists):
    final_lists = ""
    for values in lists:
        if len(values) == 3:
            for value in values:
                final_lists += value
    return final_lists
print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]))