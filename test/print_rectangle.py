# Given width and height, print a solid rectangle with *
# 5, 4 => 
# *****
# *****
# *****
# *****
def print_rectange(width, height):
  for h in range(height):
    print('*' * width)

print_rectange(5, 4)