'''num = int(input("enter number"))
if num%2 == 0:
   print(num,"even")
else:
   print(num,"odd")

num1 = int(input("enter number:"))
num2 = int(input("enter number:"))
num3 = int(input("enter number:"))
if num1>num2 and num1>num3:
  print(num1," is greater than both the numbers")
elif num2>num3 and num2>num1:
  print(num2," is greater than both the number")
else:
  print(num3," is greater than both the numbers")



list=['a','e','i','o','u']
for i in list[0:3]:
  print(i)
'''

count=int(input("Enter any num:"))
while count==0:
  print("countdown start",2*count)
  count+=1