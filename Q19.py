punc='''!@$^(){}[]?><,/-_?..'''

str1=input("Enter the string :")

str2=""

for i in str1:
    if i not in punc:
        str2+=i
        
print(str2)
        