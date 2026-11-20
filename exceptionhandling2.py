balance = 1000
try:
    amount = int(input("Enter the amount to withdraw: "))
    if amount < 0:
        raise ValueError("Amount  must be positive.")

    if amount > 1000:
        raise ValueError("Insufficient Balance")
    else:
     balance -= amount

    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Program Executed.")
