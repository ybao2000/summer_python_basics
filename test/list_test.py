# these are lists
l1 = ["apple", "pear", "banana", "peach", "cherry"]
l2 = [1, 3, 4, 5, 6, 7, 0]
l3 = ["apple", 1, "pear", 3]
t2 = (1, 3, 4, 5, 6, 7, 0)
# print(l1)
# print(l2)
# print(l3)

# use index and square bracket to get a single element
# index starts from 0
# python allows negative index (from right to left, -1, -2, ...)
v = l1[0]
print(v)

# use in to check if a value is in list
v2 = "water-melon"
res = v2 in l2
print(res)

# use index1:index2 to get sub-list
# note: end index is not included
sub1 = l1[0:2]
v3 = "banana"
print(v2 in sub1, sub1)

# sub index also can be negative
sub2 =l1[-3: -1]
print(sub2)

# if start is 0, you can omit it
sub3 = l1[:2]
sub3_2 = l1[2:]
sub3_3 = l1[3:1:-1]
print(sub3)
print(sub3_2)
print(sub3_3)

# what is i omit end, that means start from index, and include everything after the start
sub4 = l1[1:]
print(sub4)

# merge 2 lists
print(l1 + l2)

# multiply
print(l1 * 3)

###########list is mutable

# item assign -- change item
l1[0] = "watermelon"
print(l1)

# append (insert at the last) - add item
l1.append("watermelon")
print(l1)

# insert - add item
l1.insert(2, "honeydew")  
print(l1)

# extend (similar to append, but with iterable, i.e. multiple items)
l1.extend(t2)
print(l1)

print('--------------')
item = l1.pop(0)
print(item)

# remove - remove item
l1.remove('watermelon')
print(l1)

# clear - remove all items
l1.clear();

# sort
l2.sort()
print(l2)

# reverse
l2.reverse()
print(l2)

# functions can be chained only when it returns something

# pop -- remove item at a certain index
first_item = l1.pop(0)
print(l1, first_item)

last_item = l1.pop()  # if no index provided, it will remove the last one from the list
print(l1, last_item)