# find the least common mutiple for 2 numbers
def least_common_multiple(num1, num2):
  num = max(num1, num2)
  while True:
    if num % num1 == 0 and num % num2 == 0:
      return num
    num += 1

print(least_common_multiple(115, 25))