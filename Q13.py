from datetime import date
birthday =int(input("Enter you birth day :"))
birthmonth =int(input("Enter you birth month :"))
birthyear =int(input("Enter you birth year :"))
td = date.today()

age = td.year - birthyear - ((td.month, td.day) < (birthmonth, birthday))

print(age)
