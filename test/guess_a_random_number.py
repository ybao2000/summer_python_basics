import random

# randomly give a number between 1 and 10,
# keep guessing the number by input until you get the correct answer

num = random.randint(1, 50)
while True:
  guess = input("enter a number: ")  # input is reading something from keyboard (wait until you press enter)
  iGuess = int(guess)
  if iGuess == num:
    print(f"Bingo...you got the right number {num}")
    break
  elif iGuess > num:
    print(f"Your number is too high...try another guess")
  else:
    print(f"Your number is too low...try another guess")