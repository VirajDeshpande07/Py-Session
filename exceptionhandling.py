try:
    num = int(input("Enter a number : "))
    result = 10 / num
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")