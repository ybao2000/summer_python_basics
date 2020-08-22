# Probablity test: randomly given a number between 1 and 10, how many times to reproduce the same number?
# randomly generate a number, stop until number is repeated
# 1, 3, 5, 4, 2, 5
# 3, 7, 9, 10, 2, 4, 5, 4
import random
def number_to_reproduce():
  icount = 0
  s = set()
  while True:
    num = random.randint(1, 10)
    icount += 1
    if num in s:
      # return icount, num, s
      return icount
    else:
      s.add(num)

TEST_NUMBER = 200000
sum = 0
for i in range(TEST_NUMBER):
  icount = number_to_reproduce()
  sum += icount
average = sum / TEST_NUMBER

print(average)