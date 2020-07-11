# print test with name, age, height, gender
def print_info(name, age, height, gender):
  ''' this is to print information for a person

      name: str

      age: int

      height: str
      
      gender: boolean
  '''
  if gender:
    title = "Boy"
  else:
    title = "Girl"
  print(f"My name {name}. I am {age} year's old, {height} tall. I am a {title}")


# My name is Bobby. I am 9 year's old, 5'3'' tall. I am a boy
print_info("Bobby", 9, "5'3''", True)

# time to test single quote, double quote, and triple single quote, triiple double quote?????
# ieal is if the variable has single quote, please use double quote as start and end quote 5' => "5'"
#         if the variable has double quote, please use single quote as start and end quote 5" => '5"'
#         if the vailable has both single quote and double quote, what to do?
#                           5'3" => '5'3"', "5'3""
#                                => '''5'3"''' (right), """5'3"""" (wrong)