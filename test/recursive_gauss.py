# sum up from 1 to 100
# When Guass (price of math) was in elementary school,
# his math teach wants to take a break for himself,
# then he asked the student to sum up from 1 to 100

# sum = 1+2+3+4+5+6+7...+100
sum = 0
for i in range(1, 101):
  sum += i
print(sum)

# s(n) = s(n-1) + n
def s(n):
  if n==0:  # always needs a stopper
    return 0
  return s(n-1)+n # recursive call

print(s(100))