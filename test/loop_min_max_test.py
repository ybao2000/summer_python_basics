mylist = [9, 4, 222, 1, 39, 64, 77, 100]
mylist= []
# 2, first check if the list is empty or not
if mylist:
  my_min = mylist[0]
  for num in mylist:
    if num < my_min:
      my_min = num
  print("the min is ", my_min)
else:
  print("there is no value in the list")