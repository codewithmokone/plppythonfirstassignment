# Prompt the user to enter the first number
firstNumber = int(input("Enter your first number? "))

# Prompt the user to enter the second number
secondNumber = int(input("Enter your second number? "))

# prompt the user to choose an operator
operator = input("Choose your operand, (e.g. +, -, /, *)? ")

if operator == "+":
    total = firstNumber + secondNumber
elif operator == "*":
    total = firstNumber * secondNumber
elif operator == "/":
    if secondNumber == 0:
        print("Error: Division by zero is not allowed.")
        total = None
    else:
        total = firstNumber / secondNumber
else:
    total = firstNumber - secondNumber

print(firstNumber, operator , secondNumber, "=",total)