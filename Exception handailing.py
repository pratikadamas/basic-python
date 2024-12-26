
try:
   dividend = int(input("Enter the dividend: "))
   divisor = int(input("Enter the divisor: "))
   result = dividend / divisor
   print(f"Result of division: {result}")
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
except ValueError:
   print("Error: Invalid input. Please enter valid integers.")


   # ZeroDivisionError, ValueError all are pre defined in the exception handaling
   # if you enter a non-numeric value, a ValueError
