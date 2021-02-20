import random

random_number=random.randint(1, 10)

chances=5
guess=int(input("enter ur guess:"))

while  chances >5:
  if guess < random_number:
       print('Guess is too low. Try again')
  if guess > random_number:
    print('Guess is too high. Try again')
  if guess == random_number:
    break

if guess == random_number:
      print("you win")

if not chances<5:
      print("you lose number is",random_number)
