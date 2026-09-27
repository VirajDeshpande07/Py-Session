#count the number of digits in a number.
n = 12345
count = 0
while n > 0:
    count = count + 1
    n = n//10
print(count)