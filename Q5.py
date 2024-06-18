# 5. Take a string input from the user and write it on a text file.

text=input("Enter something (String):")
file_1 = open("C:\\Desktop\\Python and ML\\Piyush\\file1.txt","w")
file_1.write(text)
print("Data entered successfully.")
