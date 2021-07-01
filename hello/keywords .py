# And keyword
if 5 < 6 and "rain" != "spitfire":
    print("condition matches so it will be printed")

if 5 > 6 and "rain" == "rain":
    print("condition doesn't matcheds so it won't be printed")

value = 90
if value > 90 and value < 100:
# if 90 < value < 100:
    print("yes")
else:
    print("we're sorry")

# or keyword
if 75 > 89 or len("kill") == len("bill"):
    print("will this print?")
if 65 > 55 or len("jeopardy") == len("frere"):
    print("it sure will")
if 87 < 65 or "rain" == "pain":
    print("it won't print")

#not keyword
if "z" in "hello":
    print("this will not print")

if "h" in "helo":
    print("it will print")

if "z" not in "hello":
    print("it has to print")

value = 100
if value > 100:
    print("nope")

if not value > 100:
    print("yep")

#nested if else
ingredient1 = "pasta"
ingredient2 = "cheese"

# if ingredient1 == "pasta":
#     if ingredient2 == "cheese":
#      print("cheese pasta will be an ideal choice")
#     else:
#      print("try out the plain pasta")
# else:
#     print("I have no recommendation")

#alternate by using and keyword
if ingredient1 == "pasta" and ingredient2 == "cheese":
    print("cheese pasta")
elif ingredient1 == "pasta":
    print("eat pasta")
else:
    print("eat 5 star do nothing ")



