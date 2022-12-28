def main():
    print(a,b)

# This function adds two numbers
def addition(a, b):
    return a + b

# This function subtracts two numbers
def subtracttion(a, b):
    return a - b

# This function multiplies two numbers
def multiplication(a, b):
    return a * b

# This function divides two numbers
def division(a, b):
    return a / b


print("Please Select the operation you want")
print("1-Addition")
print("2-Subtraction")
print("3-Multiplication")
print("4-Division")

while True:
    # will take the input from the user
    numberOfOperation = input("Enter the number of the operation you want (1/2/3/4): ")

    # check if number of the operation is one of the four options
    if numberOfOperation in ('1', '2', '3', '4'):
        number1 = float(input("Please enter first number: "))
        number2 = float(input("please enter second number: "))

        if numberOfOperation == '1':
            print(number1, "+", number2, "=", addition(number1, number2))

        elif numberOfOperation == '2':
            print(number1, "-", number2, "=", subtraction (number1, number2))

        elif numberOfOperation == '3':
            print(number1, "*", number2, "=", multiplication(number1, number2))

        elif numberOfOperation == '4':
            print(number1, "/", number2, "=", division(number1, number2))
        
        # will check if the user want to do another calculation
        # will break the while loop if the answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
        
if name=="main":
    main()