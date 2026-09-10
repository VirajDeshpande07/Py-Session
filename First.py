#1.write a program to check the number is even or odd
n = int(input("enter a number: "))
result = n%2 == 0
print("Number is odd :", not result)

#2.write a program to print age in days
# output: 3 years = 1095 days
age = int(input("Enter your age in years: "))
days = age * 365
print(f"{age} years = {days} days")

#3.write a program to convertt minutes into hours and print it
#example : 135 is 2 hours 15 mintues
mins = int(input("Enter mins: "))
hours = mins // 60
rem_mins = mins%60
print(f"{mins} is {hours} hours and {rem_mins} minutes")

#4.write a program to extract the last digit of a number
number = int(input("Enter a number: "))
last_digit = number % 10
print(f"The last digit of {number} is {last_digit}")
