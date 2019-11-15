#GUESS NUMBER
from random import randint

sNumber = (randint(1,100)) #secret number
gNumber = '' #guessed number

while gNumber != sNumber:
  gNumber = int(input("Guess the number between 1 and 100! "))
  if int(gNumber > sNumber):
    print("Too high!")
  elif int(gNumber < sNumber):
    print("Too low!")   
  else:
    print("Congratulations!")

