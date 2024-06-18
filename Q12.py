# 12. Take a number and print the sum of the digits of that number.    

num=int(input("Enter a number:"))
sum=0
while(num>0):
    sum+=num%10
    num=num//10  
print("Sum of digits of the given number is ",sum)      