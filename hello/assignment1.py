# how do I convert the string “1000” to an integer? Write your code below.
print(int("1000"))

# How do I convert the floating point number 3.764 to an integer? Write the code below.
# What will be the return value?
print(int(3.764))

# In a Python program, I have my business expenses represented by a floating point number: 99.45.
# I want to express this value as a string. However, I also want to add
# - a dollar sign  in front of the amount- a space and the word “dollars” at the end
# The final result should be "$99.45 dollars".
# Write the code to make this happen.
# NOTE: Your answer must use concatenation.
# NOTE: 99.45 must start out as a floating-point value.
# You cannot use "99.45". Instead, figure out a way to convert 99.45 to a string.
print("$" + str(99.45) + " " + "dollars")
