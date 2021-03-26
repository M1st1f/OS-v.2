#I am not commenting this code since it looks self explanatory :)

def Callculator():
    "Calculaor"
    def add(x,y):
        return x + y

    def subtract(x,y):
        return x - y

    def multiply(x,y):
        return x * y

    def divide(x,y):
        return x/y

    math_time = int(input("Select operation: \n1.Add \n2.Subtract \n3.Multiply \n4.Divide \n>>> "))

    num1 = float(input("Enter first number: "))
    num2= float(input("Enter second number: "))

    if math_time == 1:
        print(num1, "+", num2, "=", add(num1, num2))
    elif math_time == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif math_time == 3:
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif math_time == 4:
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")
