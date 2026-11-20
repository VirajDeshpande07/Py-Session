#password validation:

try:
    password = input("Enter your password: ")

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    
    if not password.isalpha():
        raise ValueError("Password must contain only alphabetic characters.")

    print("Password is valid.")

except ValueError as e:
    print("Error:", e)