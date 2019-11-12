#! /bin/bash
# #########################################################
# Author: p4dl0k
# This is a user input calculator
# This is for practice
# 
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
    print(firstNumber / secondNumber)
  else:
    print("You have typed something unexpected")
  pass
   
