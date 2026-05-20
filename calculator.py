# a Simple Calculator

print("\n====== Calculator ======")
num1 = int(input('Input the first number: '))
num2 = int(input('Input the second number: '))
operation = input("Select the operation you need (+/-/x/:): ")

# The Operator Functions
def addition(num1, num2):
    return num1 +num2

def multiple(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def substraction(num1, num2):
    return num1 - num2

# The Condional Decisions
if operation == "+":
    print(addition(num1, num2))
elif operation == "-":
    print(substraction(num1, num2))
elif operation == "x":
    print(multiple(num1, num2))
elif operation == ":":
    print(division(num1, num2))
else:
    print("Operation is invalid!")
