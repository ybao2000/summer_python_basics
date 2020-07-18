# these are tuples
t1 = ("apple", "pear", "banana", "peach", "cherry")
t2 = (1, 3, 4, 5, 6, 7, 0)
t3 = ("apple", 1, "pear", 3)
# print(t1)
# print(t2)
# print(t3)

# use index and square bracket to get a single element
# index starts from 0
# python allows negative index (from right to left, -1, -2, ...)
v = t1[-1]
print(v)

# use in to check if a value is in tuple
v2 = "water-melon"
res = v2 in t2
print(res)

# use index1:index2 to get sub-tuple
# note: end index is not included
sub1 = t1[0:2]
v3 = "banana"
print(v2 in sub1, sub1)

# sub index also can be negative
sub2 = t1[-3: -1]
print(sub2)

# if start is 0, you can omit it
sub3 = t1[:2]
sub3_2 = t1[2:]
sub3_3 = t1[3:1:-1]
print(sub3)

# what is i omit end, that means start from index, and include everything after the start
sub4 = t1[1:]
print(sub4)

# merge 2 tuples
print(t1 + t2)

# multiply
print(t1 * 3)

###########tuple is not mutable
# t1[0] = "watermelon"