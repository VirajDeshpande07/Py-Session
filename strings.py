# python examples for all string operations
#1 capitalize first letter of string
string = "hello I am Viraj."
print("Capitalize string: ", string.capitalize())

#2. Strip spaces from both ends
print("Remove spaces: ",string.strip())

#3. title case (capitalize each word)
print("title case: ", string.title())

#5 count occurences of a substring
print("letter a occurs",string.count('a'),"times in the string")

#6 replace a substring
print(string.replace("hello I am Viraj","hello python is fun"))