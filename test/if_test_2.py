# if, elif, else
# involving conditions

# Given a mark between 0 and 100, grade the mark as A+, A, A-, B+, B, B-, C+, C, C-, D, F (95, 90, 85, 80, 75, 70, 65, 60, 55, 50)

# this is not good for 2 reasons
# reason one is there are too many ifs, logically not good
# reason two is inside the if/elif/else, not necessary grade =
def grade_a_mark(mark):
  if mark >= 95:  # 95, 96, 97, 98, 99, 100
    grade = "A+"
  elif mark >= 90: # 90, 91, 92, 93, 94
    grade = "A"
  elif mark >= 85: # 85, 86, 87, 88, 89
    grade = "A-"
  elif mark >= 80: # 80, 81, 82, 83, 84
    grade = "B+"
  elif mark >= 75: # 75, 76, 77, 78, 79
    grade = "B"
  elif mark >= 70: # 70, 71, 72, 73, 74
    grade = "B-"
  elif mark >= 65: # 65, 66, 67, 68, 69
    grade = "C+"
  elif mark >= 60: # 60, 61, 62, 63, 64
    grade = "C"
  elif mark >= 55: # 55, 56, 57, 58, 59
    grade = "C-"
  elif mark >= 50: # 50, 51, 52, 53, 54
    grade = "D"
  else:
    grade = "F"
  return grade

# test with random mark
# import random
# mark = random.randint(0, 100)
# grade = grade_a_mark(mark)
mark = 88
grade = grade_a_mark(mark)
print(f"your mark is {mark}, and your grade is {grade}")