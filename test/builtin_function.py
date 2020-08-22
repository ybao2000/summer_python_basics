print("hello world")

# what if I want a pi
pi = 3.141592653589793
import math   # math module (a set of functions)
print(math.pi)

import random  # random module
rnd = random.randint(1, 10)
print(rnd)

# str function - convert anything to string
a = 7
b = str(7)
# c = a+b
print(type(a), type(b))

# int function - convert string to int (only when the string contains only numbers)
c = "30303"
d = int(c)
print(c, type(c), d, type(d))

# float function - convert string to float (only when the string contains only numbers and dot)
# only convert in one step, you canot convert string of '.3' to int 0
e = '.3'
f1 = float(e)
f2 = int(f1)
print(e, type(e), f2, type(f2))
