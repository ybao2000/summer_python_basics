# Quadratic equation:
#    a x^2 + b x + c = 0
   
#    Given a (a != 0), b, c, return a list of answers
#    	if no solution, return empty list
# 	if one solution, return list with one answer
# 	if two solution, return list with two answers

import math

def quadratic_equation_solver(a, b, c):
  term = b * b - 4 * a * c
  if term > 0:
    term_2 = math.sqrt(term)
    return [(-b+term_2)/(2*a), (-b-term_2)/(2*a)]
  elif abs(term) < 1e-8:
    return [-b/(2*a)]
  else:
    return []

print(quadratic_equation_solver(2, -4, 2))