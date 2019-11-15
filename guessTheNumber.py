#GUESS NUMBER
from random import randint

sNumber = (randint(1,10)) #secret number
gNumber = '' #guessed number

while gNumber != sNumber:
  gNumber = int(input("Guess the number between 1 and 10! "))
  if int(gNumber == sNumber):
    print("Congratulations! You got it!")
  else:
    print("wrong!")
