mylist = [9, 4, 222, 1, 39, 64, 77, 100]

# find the numbers which are > 50
result = []   # initialize the result with empty list
for num in mylist:
  if num > 50:
    # print(num, end=" ")
    result.append(num)

print(result)


# exercise, get all even numbers from the list and generate that list
result2 = []
for num in mylist:
  if num % 2 == 0:
    result2.append(num)

print(result2)
