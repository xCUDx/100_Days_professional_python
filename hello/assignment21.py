# Declare a greater_sum function that accepts two lists of numbers.
# It should return the list with the greatest sum.
# You can assume the lists will always have different sums.
#
# EXAMPLES
# greater_sum([1, 2, 3], [1, 2, 4]) => [1, 2, 4]
# greater_sum([4, 5], [2, 3, 6])    => [2, 3, 6]
# greater_sum([1], [])              => [1]

def greater_sum(a,b):
    if sum(a) > sum(b):
        return a
    else:
        return b
print(greater_sum([1, 2, 3], [1, 2, 4]))

# Declare a sum_difference function that accepts two lists of numbers.
# It should return the difference between the sum of values in the first list and the second list
#
# EXAMPLES
# sum_difference([1, 2, 3], [1, 2, 4]) => 6 - 7 => -1
# sum_difference([4, 5], [2, 3, 6])    => 9 - 11 => -2
# sum_difference([1], [])              => 1
def sum_difference(c,d):
    return sum(c) - sum(d)
print(sum_difference([1, 2, 3], [1, 2, 4]))

# Given a list of floating point values
# values = [3.45, 5.67, 7.89]
# provide the code to get list of squares of the values using both
# (1) list comprehension and (2) the map function.
values = [3.45, 5.67, 7]
print(list(value ** 2 for value in values))

print(list(map(lambda value:value ** 2, values)))