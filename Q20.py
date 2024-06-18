l1=[]
size=int(input("Enter the size of list:"))

for i in range(size):
    num=int(input("Enter the number you want to enter in the list:"))
    l1.append(num)
    
sum=0
for i in range(size):
    sum+=l1[i]
    
print("The sum of all elements of the list",sum)