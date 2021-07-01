import sys
print(sys.argv)
print(type(sys.argv))
word_length = 0
for arg in sys.argv[1:0]:
    word_length += len(arg)
    print(f"total length of all command line arguments is {word_length}")
