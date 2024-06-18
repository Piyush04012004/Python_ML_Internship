str1=input("Enter a string: ")
str2=input("Enter another string: ")

if len(str1)!=len(str2):
    print("Not anagram.")
else:
    if sorted(str1)==sorted(str2):
        print("Both strings are anagram.")   
    else:
        print("Not anagram.")    