# for loop is usually going throught an iterable container (tuple, list, set, dictionary, range(), string)

# first, how to count
mylist = [9, 4, 222, 1, 39, 64, 77, 100]
# print(len(mylist))

# when you do the count for a container, 
# step 1: initialize a variable, set the variable to 0
# step 2: iterate throught container using for loop
#         everytime, just increate the varaible by 1
# finally, the variable is the count

# mycount = 0
# print("initial", mycount)
# for num in mylist:
#   mycount = mycount + 1
#   # mycount + 1
#   print(mycount)

# print("final", mycount)


# sum of the numbers
# sum = 0
# print("initlal sum", sum)
# for num in mylist:
#   sum = sum + num
#   # sum += num
#   print(sum)

# print("final sum", sum)

# exercise, find the average of the numbers
# average = sum /count

# mycount = 0
# sum = 0
# print("initlal count", mycount, "initial sum", sum)
# for num in mylist:
#   mycount = mycount + 1
#   sum = sum + num
#   # sum += num
#   print(mycount, sum)

# print("finalcount", mycount, "final sum", sum)
# print("average", sum/mycount)

# find the max of the numbers
# print(max(mylist))
# we want to use loop to find the maximum
# same trick: we initialize a variable, but be careful here, don't set it as 0
# then how to initialize it? many ways, I will introduce 2 ways
# step 1: initialize 
# 1. init it as None
mylist = [10000, 20000, 30000, 50000]
# a = None
# print(a)
# step 2: loop through the numbers, and compare the number with the variable
#         if a is None, no compare, just replace a with the number
#         otherwise (else), do comparison, replace only when the number > variable
# after the loop, the variable is the answer
my_max = None
for num in mylist:
  # if my_max is None:
  #   my_max = num
  # else:
  #   if num > my_max:
  #     my_max = num
  if my_max is None or num > my_max:
    my_max = num
  # print(my_max)

print("the max is", my_max)

# exerise, please find the minimum
# print(min(mylist))
my_min = None
for num in mylist:
  if my_min is None or num < my_min:
    my_min = num
  print(my_min)

print("the min is ", my_min)

