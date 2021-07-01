# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""

def encrypt_message(values):
    alphabet = "abcdefghijklmnnopqrstuvwxyz"
    new_value = []
    for value in values:
        temp_value = (alphabet.index(value) + 2) % 26
        new_value += alphabet[temp_value]
    return new_value
print(encrypt_message("abc"))


