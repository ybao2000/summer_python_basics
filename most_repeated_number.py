# Given a list of 100 numbers ranged between 1 and 10, find the most repeated number. 
def most_repeated_number(numbers):
  # first step, generate a dictionary: kvp => key is the number, value is the occurence
  dict_num = {}
  for number in numbers:
    if number in dict_num:
      # dict_num[number] = dict_num[number] + 1
      dict_num[number] += 1
    else:
      dict_num[number] = 1
  print(dict_num)
  
  # second step, find the key and value that has the biggest number
  kvp_result = ()
  for kvp in dict_num.items():
    if not kvp_result:
      kvp_result = kvp
    else:
      if kvp[1] > kvp_result[1]:
        kvp_result = kvp
  return kvp_result[0]

import random
numbers = []
for i in range(100):
  numbers.append(random.randint(1, 10))

print(numbers)
print(most_repeated_number(numbers))
