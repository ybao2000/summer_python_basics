# find the greast common divisor of 2 numbers
def greatest_common_divisor(num1, num2):
  # algorithm:
  # intialize the result with 1
  # for loop from 1 to min(num1, num2) -- loop from smaller to bigger
  #    check num to see if num is a common divisor, if yes, then update result
  # after the loop the result is the answer

  cd = 1
  for num in range(2, min(num1, num2)):
    if (num1 % num == 0) and (num2 % num == 0):
      cd = num

  # return cd

  # algorithm 2:
  # loop from bigger to smaller

def greatest_common_divisor(num1, num2):
  for num in range(min(num1, num2), 0, -1):
    if (num1 % num == 0) and (num2 % num == 0):
      return num

print(greatest_common_divisor(5555, 2255))


