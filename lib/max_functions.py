def max_of_two(num1, num2):
  if num1 < num2:
    return num2
  else:
    return num1

# n = max_of_two(3, 5)
# print(n)

def max_of_three(num1, num2, num3):
  # return max(num1, num2, num3)
  # there are two ways
  # if num1 < num2:
  #   if num2 < num3:
  #     return num3
  #   else:
  #     return num2
  # else:
  #   if num1 < num3:
  #     return num1
  #   else:
  #     return num3

  m = max_of_two(num1, num2)
  return max_of_two(m, num3)

  # for experienced developer
  # return max_of_two(max_of_two(num1, num2), num3)

# n = max_of_three(3, 7, 5)
# print(n)