#! /bin/bash
# #########################################################
# Author: p4nd4_chz

# This will be the welcome page. Here there will be options
# available to access different programs written to purpose
#
# This just is for practice
# 
# #########################################################

greeting = "Hello! I am your accountant."

# #########################################################
#
# WHAT WOULD YOU LIKE TO DO?
# 
# options will include: 
#
# addAbill
# addAcheck
# viewReport 
# --daily, weekly, monthly, yearly
# 
# 
# #########################################################


A = addAbill = #start addAbill module
B = addAcheck = #start addAcheck module
C = viewReport = #start viewReport module

menuOption = input("What would you like to do?" + "\n " + "\n(A) ADD A BILL \n(B) ADD A CHECK \n(C) QUICKVIEW \n(D) VIEW REPORTS" +"\n " "\ninput: ")


if (menuOption == 'a' or 'A'):
  print("Add a bill...") #kill process -- start addAbill module
elif (menuOption == 'b' or 'B'):
  print("Add a check...") #kill process -- start addAcheck module
elif (menuOption == 'c' or 'C'):
  print("Quick Report...") #kill process -- print quickReport
elif (menuOption == 'd' or 'D'):
  print("View Reports...") #kill process -- start viewReport module
else:
  print("Please type the number 1, 2, 3, or 4.")



