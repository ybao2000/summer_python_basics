# str ==> string
myFirstName = "Frank"
anotherFirstName = "frank"
print(type(myFirstName), myFirstName == anotherFirstName)

myFirstName = "Frank"

# number 
#  int (integer) 
#  int => exact
a = 7
a1 = 7
print(a == a1)
print(type(a))

#  float (with decimal)
#  float => not exact, tolerance
b = 7.0
print(type(b))
b1 = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
b2 = 0.9
print(b1, b2, b1==b2)

# bool, boolean
c = True
d = False
print(c, d, c == d)