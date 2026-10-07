# # python examples for all string operations
# #1 capitalize first letter of string
# string = "hello I am Viraj."
# print("Capitalize string: ", string.capitalize())

# #2. Strip spaces from both ends
# print("Remove spaces: ",string.strip())

# #3. title case (capitalize each word)
# print("title case: ", string.title())

# #5 count occurences of a substring
# print("letter a occurs",string.count('a'),"times in the string")

# #6 replace a substring
# print(string.replace("hello I am Viraj","hello python is fun"))

# #7 String lowercase
# print("Lowercase string: ", string.lower())

# #8 String uppercase
# print("Uppercase string: ", string.upper())

# # accept a string from user and count the vowels from it without using for loop
# s = input("Enter a string: ")

# count = s.lower().count('a') + s.lower().count('e') + s.lower().count('i') + s.lower().count('o') + s.lower().count('u')

# print("Number of vowels:", count)

# # add 3 strings
# str1 = "ha"
# str2 = "ha"
# str3 = "ha"
# print(str1+str2+str3) 

# str = 'ha'
# print (str*3)

# string = input("enter your name: ")
# print("occurences of letter a are: ", string.count('a'))

#using substring and replace function replace a with z
# string = 'viraj'
# print(string.replace("a","z"))

#split name in 2 parts
# string = "viraj"
# name = [string[:3], string[3:]]

# print(name)

# sort the name 
# string = "viraj"
# sorted_string = sorted(string)
# print(sorted_string)

# empty list
# my_list = []
# # add elements to the list
# fruits = ["apple", "mango"]
# my_list.extend(fruits)
# print(my_list)

#length function gives no if elements in the list
# nums = [1, 2, 3, 4, 5]
# print(len(nums))
# #sum
# print(sum(nums))
# #sorting
# nums = [5, 2, 8, 1, 3]

# print(sorted(nums))
# print(sorted(nums, reverse=True))

#create a list of 10 numbers and display the sum of last 4 elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(nums[-4:]))
#remove the items from the list located at 2nd and 5th position.
print("Before removing elements:", nums)
nums.pop(1)  
nums.pop(3)   
print("After removing 2nd and 5th elements:", nums)
#print the difference between the highest and smallest number in the list.
print("Difference between highest and smallest number:", max(nums) - min(nums))
#append a new element in the list which is half of the item of 3rd postion in the list.
