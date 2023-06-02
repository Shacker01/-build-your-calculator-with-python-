num1 = input ("Enter first number: ")
operator = input ("Input your operation sign, '*,-,+,/,^,%: ")
num2 = input ("Enter second number: ")
#num2_prompt = input ("Enter second number: ")
#num2 = input (num2_prompt)

#while not num2.isdigit():
 # print ("Enter a digit number!")
#  num2 = input (num2_prompt)
  
num1 = int(num1)
num2 = int (num2)

if operator == "+":
  result= num1 + num2
elif operator == "-":
  result = num1 - num2
elif operator == "*":
  result= num1 * num2
elif operator == "^":
  result = pow(num1, num2)
elif operator == "%":
  result = num1 % num2
elif operator == "/":
  result = num1 / num2
else:
  print ("Invalid input! enter a valid operator")
print (f"{num1} {operator} {num2}  = {result}")
