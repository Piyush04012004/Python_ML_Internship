num1=int(input("Enter a number : "))
num2=int(input("Enter another number : "))
operator=input("Enter any mathematical operand (+,-,*,/,%) : ")

if(operator=='+'):
    print("Sum = ",num1+num2)
elif(operator=='-'):
    print("Difference = ",num1-num2)
elif(operator=='*'):
    print("Product = ",num1*num2)
elif(operator=='/'):
    print("Quotient = ",num1/num2)
elif(operator=='%'):
    print("Reminder = ",num1+num2)
else:
    print("Enter the valid operator!!")                    