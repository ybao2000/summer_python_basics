import math
def triangle_area(base, height):
  return base * height/2.0

def triangle_area_2(a, b, c):
  s = (a + b + c)/2
  return math.sqrt(s * (s-a) * (s-b) * (s-c))

print(triangle_area_2(3, 4, 5))