# print january

#          1  2  3  4
# 5  6  7  8  9  10 11
# 12 13 14 15 16 17 18
# 19 20 21 22 23 24 25
# 26 27 28 29 30 31

print("          1  2  3  4")
print("5  6  7  8  9  10 11")
print("12 13 14 15 16 17 18")
print("19 20 21 22 23 24 25")
print("26 27 28 29 30 31")
print()

def print_month(title, indent, number):
  print(title)
  print('   ' * indent, end='')
  for i in range(1, number+1):
    print(f"{i:2d}", end=' ')
    if (i+indent) % 7 == 0:
      print()

print_month('Jan', 3, 31)
print()
print_month('Feb', 6, 29)