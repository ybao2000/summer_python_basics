# join: stick the items in the list together

items = ["Funny", "Cat", "Garfield", "Dressed", "As", "Easter", "Bunny"]
text = " ".join(items)

print(text)

# this is to get the first letter of the words in the text
b = [item[0] for item in items]

print("".join(b))

