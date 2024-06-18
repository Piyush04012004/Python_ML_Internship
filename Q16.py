str1=input("Enter a string : ")
l1=list(str1)
# print(l)
freq=[l1.count(ele)for ele in l1]
d1=dict(zip(l1,freq))
print(d1)