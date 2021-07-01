# def output_text():
#     pass

def output_text():
    print("hello")
    print("welcome")
    print("thank you")
output_text()
output_text()

def p(text):
    print(text)
p("hi")
p(5 + 4)

def add(a,b):
    print("The sum of", a,"and", b,"is", a + b )
add(5,3)
add(6,-3)

def add(a,b,c):
    print("sum of the numbers is", a + b + c)
add(3,4,5)

def add(a,b,c):
    return a+b+c
result = add(3,5,1)
print(result)

def add(a=0, b=0, c=0):
    return(a+b+c)
print(add())

#None type
a = None
print(type(a))

#Function annotation
def word_multiplier(a: str, b: int ) -> int:
    return a * b
print(word_multiplier("hello",3))

# def product(a,b):
#     return a*b
# product(a=5)
