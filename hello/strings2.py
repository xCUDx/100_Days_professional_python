#method "find"
browser = "google chrome"
print(browser.find("gc"))
print(browser.find("g"))
print(browser.find("o",3))
print(browser.find("o"))

print("rome" in browser)
print("tome" in browser)

#method "index"
print(browser.index("ch"))
#print(browser.index("hc"))

#r.find
str1 = "hello my name is John what is your name sir"
print(str1.rfind("i"))

#startswith
word = "Python is an AI ML related language"
print(word.startswith("P"))
print(word.endswith("age"))
print(word.endswith("Language"))

# word.count
word = "queueing"
print(word.count("ue"))
print(word.count("r"))
print(word.count("e") + word.count("u"))

#capitalize , title, lower , upper , swapcase
story = "Long ago there lived an idiot"
print(story.capitalize())
print(story.title())
print(story.upper())
print(story.lower())
story = story.upper()
print(story)
print(story.lower().title())
print("hElLo".swapcase())

#boolean for strings
print(story.islower())
print(story.isupper())
print(story.istitle())

print("area 51" .isalpha())
print("area" .isalpha())
print("51".isnumeric())
print("area51" .isalnum())
print("area 51".isalnum())
print(" ".isspace())
print(" ; ".isspace())

#removing spaces .lstrip, rstrip, strip
line = "          hello         "
print(line.lstrip())
print(len(line.lstrip()))
print(len(line))
print(line.rstrip())
print(line.strip())
print(len(line.strip()))

link = "www. python.org"
print(link.lstrip("w"))
print((link.rstrip("org")))
print((link.strip("worg")))
print(link.strip("w.org"))

#replace method
phone_number = "222 333 4567"
print(phone_number.replace("2", "7", 3))
print(phone_number.replace(" ", "-"))
phone_number = print(phone_number.replace(" ", "-"))