f1=open("file1.txt",mode='r',encoding='utf-8')
f2=open("file2.txt",mode='w',encoding='utf-8')

data=f1.readlines()
for line in data:
    f2.write(line)

f1.close()
f2.close()
