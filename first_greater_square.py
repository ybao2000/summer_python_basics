#Find the first square number that is greater than a give number
# 16, => 17, 25 => 25
# 80, => 81
# algorithm is using while loop
# initialize index with 1
# while loop with condition of True
#      square the index, and compare the square with the number, if square is > number, return the square
#      increase the index (otherwise, you will get infinite loop)
def first_greater_square(number):
  index = 1
  while True:
    square = index * index
    if square > number:
      return index, square
    index += 1

# print(first_greater_square(117))
import random
number = random.randint(1, 10000)
index, square = first_greater_square(number)
print(f"number: {number}, first grader index, square: {index}, {square}")