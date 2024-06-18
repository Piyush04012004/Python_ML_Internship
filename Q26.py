str1=input("Enter a string value : ")
pre=input("Enter a prefix to check in above string : ")
suf=input("Enter a suffix to check in the above string : ")

if str1.startswith(pre):
    print("It starts with the followig prefix mentioned.")
elif str1.endswith(pre):
    print("It ends with the followig suffix mentioned.")    
else:
    print("Neither it starts with the followig prefix mentioned nor it ends with the following suffix mentioned.")
    

