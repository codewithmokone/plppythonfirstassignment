# Prompt the user to enter the first number
firstNumber = int(input("Enter your first number? "))

# Prompt the user to enter the second number
secondNumber = int(input("Enter your second number? "))

# prompt the user to choose an operator
operator = input("Choose your operand, (e.g. +, -, /, *)? ")

# Perform the calculation based on the chosen operator
if operator == "+":
    # Addition operator
    total = firstNumber + secondNumber
elif operator == "*":
    # Multiplication operator
    total = firstNumber * secondNumber
elif operator == "/":
    # Division operator with error checking
    if secondNumber == 0:
        # Handle division by zero
        print("Error: Division by zero is not allowed.")
        total = None
    else:
        total = firstNumber / secondNumber
else:
    # Substraction operator
    total = firstNumber - secondNumber

# Output the results of calculation
print(firstNumber, operator , secondNumber, "=", total)