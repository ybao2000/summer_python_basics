sum = 0
for i in range(1, 101, 2):   # 2 is the increase step  
  if i > 50:
    break
  sum += i     # sum = sum + i
else:
  print("this is else block")   
print(sum)


sum = 0
i = 1
while i < 101:
  if i > 50:
    break
  sum += i
  i += 2
print(sum)