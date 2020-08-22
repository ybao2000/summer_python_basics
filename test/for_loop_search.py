mylist = [9, 4, 222, 50, 1, 39, 64, 77, 100, 77, 64, 61]
# index ????????
# for list, index is just a sequential number, starting from 0, increase by 1


# please find index that has the number 64, if not find, please return -1
myindex = -1
target = 64
mylen = len(mylist)
for i in range(mylen):
  if mylist[i] == target:  # we found it!
    myindex = i
    break   # break means stop the loop

print(myindex)


# for i in range(10):
#   for j in range(10): or while ...
#     if i + j > 10:
#       break   # break only stop the inner loop, it doesn't affect the outer loop

# exercise, please find in the list, two numbers which sum up at 100 (guarantee there is one and only one answer)
# brute force algorithm
# target = 100
# for num1 in mylist:
#   for num2 in mylist:
#     if num1 + num2 == 100:
#       print("the answer is" , num1, num2)
#       break

# this is going to loop through index, instead of the list
# index is from 0, ...., len-1
target = 100
mlen = len(mylist)
for i1 in range(mlen):





   

