import math

def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        # operand must not divide by zero
        return num1 / num2 if num2 != 0 else "Divide by zero. "
    elif operator == "^":
        return math.pow(num1, num2)
    else: # rest of the operators are invalid
        return "Invalid operator. "

while True: 
    print('Please enter a simple math expression, enter "quit" to quit')
    expression = input("Format: num1 operator num2: ")

    if expression == "quit":
        print("Calculator finished. ")
        break

    num1, operator, num2 = expression.split()
    num1, num2 = float(num1), float(num2)

    print("Result: ", calculator(num1, num2, operator))
