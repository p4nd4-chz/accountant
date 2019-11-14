#practice practice pracitce


result = 0
i = 0

while i < 4:
  nr = int(input("Please give me a number"))
  result += nr
  i += 1
print("The result of adding numbers is: ", result)


# IS THE SAME AS

result = 0

for i in range(4):
  nr = int(input("Please give me a number: "))
  result += nr
print("The result of adding numbers is: ", result)


#while loops and for

result = 0
i = 0

while i < 3:
  x = int(input("Enter a positive number"))
  if (x>0):
    result += x
  else:
    print("NONONO! I said a POSITIVE number")
    continue
  print("Current addition result= ", result)
  i += 1
  
