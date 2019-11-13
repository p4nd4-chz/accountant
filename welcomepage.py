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

menuOption = input("What would you like to do?" + "\n " + "\n(1) ADD A BILL \n(2) ADD A CHECK \n(3) QUICKVIEW \n(4) VIEW REPORTS" +"\n " "\ninput: ")

while True:
  if (menuOption == '1'):
    print("Add a bill...") #kill process -- start addAbill module
  elif (menuOption == '2'):
    print("Add a check...") #kill process -- start addAcheck module
  elif (menuOption == '3'):
    print("Quick Report...") #kill process -- print quickReport
  elif (menuOption == '4'):
    print("View Reports...") #kill process -- start viewReport module
  else:
    print("Please type the number 1, 2, 3, or 4.")


