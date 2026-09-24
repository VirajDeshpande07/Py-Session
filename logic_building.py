# for i in range (1,5):
#     for j in range (1,(4-i)+1):
#         print(" ", end="")
#     for k in range (1,(i*2-1)+1):
#         print("*", end="")
#     print()
 
# i = 56789
# count = 0
# while i > 0:
#     i = i // 10
#     count +=1
# print(count)

n = 1234
rev = 0

while n != 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10

print(rev)