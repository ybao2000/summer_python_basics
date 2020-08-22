# Given width and height, print a solid right triangle with *
# 5, 4
# *
# **
# ***
# ***
# *****
def print_right_triangle(width, height):
  for h in range(height):
    # w = h * width  / height
    w = h * (width-1) / (height-1) + 1   # consider offset
    iw = int(w)
    print('*' * iw)

print_right_triangle(10, 7)