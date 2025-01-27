import math
import numpy as np
from sympy import symbols, solve, diff, integrate
from sympy import sympify

degree_mode = True  

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y
def power(x, y): return x ** y
def sqrt(x): return math.sqrt(x)
def log(x, base=10): return math.log(x, base)
def exp(x): return math.exp(x)
def factorial(x): return math.factorial(int(x))

def convert_angle(x):
    return math.radians(x) if degree_mode else x

def sin(x): return math.sin(convert_angle(x))
def cos(x): return math.cos(convert_angle(x))
def tan(x): return math.tan(convert_angle(x))

def solve_equation(eq):
    x = symbols('x')
    eq = sympify(eq) 
    return solve(eq, x)

def differentiate(eq):
    x = symbols('x')
    eq = sympify(eq) 
    return diff(eq, x)

def integrate_expression(eq):
    x = symbols('x')
    eq = sympify(eq) 
    return integrate(eq, x)

def matrix_operations():
    print("Matrix Operations:")
    print("1. Addition  2. Subtraction  3. Multiplication  4. Determinant")
    choice = input("Enter choice: ")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter first matrix elements row-wise:")
    matrix1 = np.array([list(map(float, input().split())) for _ in range(rows)])
    print("Enter second matrix elements row-wise:")
    matrix2 = np.array([list(map(float, input().split())) for _ in range(rows)])
    if choice == '1':
        return matrix1 + matrix2
    elif choice == '2':
        return matrix1 - matrix2
    elif choice == '3':
        return np.dot(matrix1, matrix2)
    elif choice == '4':
        return np.linalg.det(matrix1)
    else:
        return "Invalid choice"

def calculator():
    global degree_mode
    while True:
        print("\nScientific Calculator")
        print("-------------------------------------------------")
        print("|  1. Add       |  2. Subtract  |  3. Multiply   |")
        print("|  4. Divide    |  5. Power     |  6. Sqrt       |")
        print("|  7. Log       |  8. Exp       |  9. Factorial  |")
        print("| 10. Sine      | 11. Cosine    | 12. Tangent    |")
        print("| 13. Solve Eq  | 14. Differentiate | 15. Integrate |")
        print("| 16. Matrix Ops| 17. DEG/RAD   | 18. Exit       |")
        print("-------------------------------------------------")
        
        choice = input("Enter choice (1-18): ")
        if choice == '18':
            print("Exiting calculator. Goodbye!")
            break
        if choice == '17':
            degree_mode = not degree_mode
            mode = "Degrees" if degree_mode else "Radians"
            print(f"Switched to {mode} mode.")
            continue
        
        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operations = {'1': add, '2': subtract, '3': multiply, '4': divide, '5': power}
            result = operations[choice](num1, num2)
        elif choice in ['6', '7', '8', '9', '10', '11', '12']:
            num = float(input("Enter number: "))
            operations = {'6': sqrt, '7': log, '8': exp, '9': factorial, '10': sin, '11': cos, '12': tan}
            result = operations[choice](num)
        elif choice == '13':
            eq = input("Enter equation (use 'x' as variable): ")
            result = solve_equation(eq)
        elif choice == '14':
            eq = input("Enter expression to differentiate (use 'x' as variable): ")
            result = differentiate(eq)
        elif choice == '15':
            eq = input("Enter expression to integrate (use 'x' as variable): ")
            result = integrate_expression(eq)
        elif choice == '16':
            result = matrix_operations()
        else:
            print("Invalid input, please try again.")
            continue
        
        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
