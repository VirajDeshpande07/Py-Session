#write a program to swap 2 variables without using a third variable, using arithmetic operations 
#example before swap a=10, b=20 after swap a=20, b=10
a = 10
b = 20
print("Before swap a= ", a, "b= ",b)
a = a + b
b = a - b
a = a - b
print("After swap a= ",a , "b: ", b)