# dictionary uses kvp - key value pair, k:v
# all keys are unique (values not necessary unique)

d1 = {"apple": 1, "pear": 2, "banana": 3, "peach": 4, "cherry": 5, "apple": 2}
d2 = {"abby": 10, "bobby": 11, "samantha": 7, "sam": 5}
d3 = {1: "apple", 2: "pear", 3: "apple", 4: "peach"}

print(d1)
print(d2)
print(d3)

# does dictionary has index? 
# no index, because dictionary use key, not index
print(d1["apple"])
print(d3[1])

# use in to check if a key is in dictionary
k2 = "water-melon"
res = k2 in d1
print(res)

# del - delete kvp 
del d1["apple"]
print(d1)

# add/update kvp - d1[k] = v
d1["water-melon"] = 5
print(d1)

# key or value not necessary the same type
d1[5] = "water-melon"
print(d1)

# items()
print(type(d1.items()))
print(d1.items())
 
# keys()
print(type(d1.keys()))
print(d1.keys())

# values()
print(type(d1.values()))
print(d1.values())