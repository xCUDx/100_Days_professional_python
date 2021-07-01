# Define a long_word function that accepts a string.
# The function should return a Boolean that reflects whether the string has more than 7 characters.
#
# EXAMPLES:
# long_word("Python")         => False
# long_word("magnificent")    => True

def long_word(a):
    return bool(len(a) > 7)
print(long_word("hello"))
print(long_word("giraffe"))

# Define a first_longer_than_second function that accepts two string arguments.
# The function should return a True if the first string is longer than the second
# and False otherwise (including if they are equal in length).
#
# EXAMPLES:
# first_longer_than_second("Python", "Ruby")     => True
# first_longer_than_second("cat", "mouse")       => False
# first_longer_than_second("Steven", "Seagal")   => False

def first_longer_than_second(a, b):
    return bool(len(a) > len(b))
print(first_longer_than_second("hello", "hi"))
print(first_longer_than_second("no", "yes"))

# Define a same_first_and_last_letter function that accepts a string as an argument.
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters.
#
# EXAMPLES:
# same_first_and_last_letter("runner")   => True
# same_first_and_last_letter("Runner")   => False
# same_first_and_last_letter("clock")    => False
# same_first_and_last_letter("q")        => True
def same_first_and_last_letter(word):
    return (word[0] == word[-1])
print(same_first_and_last_letter("quant"))
print(same_first_and_last_letter("HIH"))


#Define a three_number_sum function that accepts a 3-character string as an argument.
# The function should add up the sum of the digits of the string.
# HINT: You’ll have to figure out a way to convert the string-ified numbers to integers.
#
# EXAMPLES:
# three_number_sum("123")   => 6
# three_number_sum("567")   => 18
# three_number_sum("444")   => 12
# three_number_sum("000")   => 0
def three_number_sum(number):
     return int(number[0]) + int(number[1]) + int(number[2])
print(three_number_sum("123"))
