#[expr_of_x for x in list_x if predicate_of_x]

a = [1, 5, 23, 34, 309, 3030, 321]
# b = [2, 6, 24, 35, 310, 3031, 322]
# b = []
# for item in a:
#   b.append(item+1)
# print(b)

# migrate the list
b = [x-1 for x in a]
print(b)

# return me the even numbers
# b = []
# for item in a:
#   if item % 2 == 0:
#     b.append(item)
# print(b)
c = [x//2 for x in a if x % 2 == 0]
print(c)

d = [1, "apple", 3, "bee", 4, "fly", 5, "banana"]
# filter out all the strings, and only return numbers
e = [x for x in d if isinstance(x, str)]
print(e)