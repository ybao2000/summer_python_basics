# for loop for tupe, list and string
l1 = ["apple", "pear", "banana", "peach", "cherry"]
t3 = ("apple", 1, "pear", 3)
s = "this is a string"
for item in l1:
  print(item)

for item in t3:
  print(item)

for item in s:
  print(item)

# for loop for range()
# sum from 1 to 100 => sum = 1+2+3+...+100 = ? (This is a famous story of Gauss, who is the math prince) => 101 *50
# range(start, end, inc) => start is the startign value, end is stopped (excluded), inc is increment value (by default, 1)
sum = 0
for num in range(1, 101, 2): # => 1, 3, 5, ... 99
  sum = sum + num
print(sum)

# for loop can be nested
# grid of coordinate:
# (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)
# (2, 1).....
# (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
for x in range(1, 6): # for row
  for y in range(1, 6):  # for column
    print(f"({x}, {y})", end=', ')
  print()