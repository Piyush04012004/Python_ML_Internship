# 3. Find the factorial of a number.

num=int(input("enter a number:"))

fact=1

if num<0:
    print("The number is negative which doesn't have factorial")
elif num==0:
    print("number is 0 and it's factorial is 1")    
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of",num,"is",fact) 