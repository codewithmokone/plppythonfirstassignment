firstNumber = int(input("Enter your first number? "))
secondNumber = int(input("Enter your second number? "))
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