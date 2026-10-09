#4. Print the sum of the digits.
num = int(input("Enter any number: "))
sum_of_digits = 0
while num > 0:
    digit = num%10
    sum_of_digits+=digit
    num //= 10
print(f"Sum of digits: {sum_of_digits}")