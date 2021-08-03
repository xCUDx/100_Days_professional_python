#the split function
users = "bob, jack ,harry ,justin ,bethoven"
print(users.split(" "))
print(users.split(",",3))

sentence = "I am learning how to code"
words = sentence.split(" ")
print(words)

#the joint function
address = ["500 fifth avenue", "New York", "NY", "10036"]
print(",".join(address))
print(":".join(address))

print("?".join(["222","333","444"]))
print("-".join(["222","333","444"]))