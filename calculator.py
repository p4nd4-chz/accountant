#! /bin/bash
# #########################################################
# Author: p4dl0k
# This is a user input calculator
# This just is for practice
# I repeat, this is only a test.
# #########################################################

while True:
  menuOption = input (" (+)add (-)subtract (*)multiple (/)divide: ") #user select math type
  firstNumber = int(input("First number: ")) #user input first number
  secondNumber = int(input("Second number: ")) #user input second number

  if (menuOption == '+'):
    print(firstNumber + secondNumber)
  elif (menuOption == '-'):
    print(firstNumber - secondNumber)
  elif (menuOption == '*'):
    print(firstNumber * secondNumber)
  elif (menuOption == '/'):
    if (secondNumber == 0):
      print('you can not do that!')
    else:
      print(firstNumber / secondNumber)
    
  else:
    print("You have typed something unexpected")
