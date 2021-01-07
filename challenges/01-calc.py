# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.




# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

#select a function 
#function = input('add','subtract','multiply','divide')

while True:
    # Take input from the user
    choice = input("Enter choice(add/subtract/multiply/divide): ")

    # Check if choice is one of the four options
    if choice in ('add', 'subtract', 'multiply', 'divide'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'add':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'subtract':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'multiply':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'divide':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")