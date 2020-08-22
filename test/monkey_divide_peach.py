# Five monkeys wanted to divide a bunch of peaches. 
# But they found that the peaches could not be divided evenly. 
# It was evening so they decided to divide those peaches next morning. 

# However, in the midnight, one monkey woke up so he quietly divided all peaches into 5 piles, 
# and found one left after division. 
# So he ate the left one, took his one fifth portion, and remixed the rest peaches. 

# Sometime later, another monkey woke up and tried to divide peaches. 
# So he divided all peaches into 5 piles, also found one left after division. 
# So he ate the left one, took his one fifth portion, and remixed the rest peaches. 

# The rest three monkeys did exactly the same thing.
#  
# Question: How many peaches were there at least in the beginning?

def is_valid_total(total):
  # monkey 1
  if total % 5 != 1:
    return False
  pile1 = (total-1) // 5

  # monkey 2
  total2 = pile1 * 4
  if total2 % 5 != 1:
    return False
  pile2 = (total2-1) // 5

  # monkey 3
  total3 = pile2 * 4
  if total3 % 5 != 1:
    return False
  pile3 = (total3 -1) // 5

  # monkey 4
  total4 = pile3 * 4
  if total4 % 5 != 1:
    return False
  pile4 = (total4 -1) // 5

  # monkey 5
  total5 = pile4 * 4
  if total5 % 5 != 1:
    return False
  return True

# print(is_valid_total(121))

def is_valid_total(total):
  for i in range(5):
    if total % 5 != 1:
      return False
    pile = (total-1) // 5
    total = 4 * pile
  return True

total = 1
while not is_valid_total(total):
  total += 1

print(f"The first valid number is {total}")


