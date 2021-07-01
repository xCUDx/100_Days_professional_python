def statement_positive_or_negative(value):
    # value = int(input("enter the value please: "))
    if value > 0:
        return "positive"
    elif value < 0:
        return "negative"
    else:
        return "it's just zero dude"
print(statement_positive_or_negative(0))
print(statement_positive_or_negative(-65))

def calculator(operation , a, b):
    if operation == "add":
        return a+b
    elif operation == "sub":
        return a-b
    elif operation == "mul":
        return a*b
    elif operation == "div":
        return a/b
    else:
        return "This is an ordinary calculator so don't become Einstein"
print(calculator("add",3,5))
print(calculator("hy",1,2))
print(calculator("mul",5,6))


