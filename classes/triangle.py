import math
class Triangle:
  # content: attributes a, b, c, methods: area
  a = 3 # these are attributes
  b = 4
  c = 5

  #magic function __init__
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def area(self): # method can use your attributes
    s = (self.a + self.b + self.c)/2
    return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

t = Triangle(3, 4, 5)  # t is an Triangle object
print(t.a, t.b, t.c)  # using . to get the arribute of an object
print(t.area())

t2 = Triangle(5, 12, 13)
# t2.a = 5
# t2.b = 12
# t2.c = 13
print("t2", t2.a, t2.b, t2.c)
print("t2 area", t2.area())

t3 = Triangle(5, 6, 7)
