# these are sets 
# no sequences, i.e., no index
# no duplicates
s1 = {"apple", "pear", "banana", "peach", "cherry", "apple"}
s2 = {1, 3, 4, 5, 6, 7, 0, 1}
s3 = {"apple", 1, "pear", 3}
print(s1)
print(s2)
print(s3)

# use in to check if a value is in set
v2 = "water-melon"
res = v2 in s1
print(res)

# set cannot be merged

###########set is also mutable

# add - add item (no sequence)
s1.add("water-melon")
print(s1)

# remove - remove item
s1.remove("apple")
print(s1)

# dont' remove item that is no in the set
# s1.remove("orange")

# discard - remove item if it exists, otherwise, don't do anything
s1.discard("apple")

# pop - randomly pick up an item from the set, remove it from the set and return the removed one
item = s1.pop()
print(item)

# clear - remove all  items from the set
s1.clear()
print(s1)
