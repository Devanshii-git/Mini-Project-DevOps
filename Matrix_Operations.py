import math  # Importing the math module for advanced mathematical functions
import numpy as np  # Importing numpy for matrix operations

class Matrix_operations:
    # Define a method for performing matrix operations
    def matrix_operations():
        # Display the available matrix operations to the user
        print("Matrix Operations:")
        print("1. Addition  2. Subtraction  3. Multiplication  4. Determinant")
        
        # Get the user's choice of operation
        choice = input("Enter choice: ")
        
        # Input the dimensions of the matrices
        rows = int(input("Enter number of rows: "))  # Number of rows
        cols = int(input("Enter number of columns: "))  # Number of columns
        
        # Input the elements of the first matrix row-wise
        print("Enter first matrix elements row-wise:")
        matrix1 = np.array([list(map(float, input().split())) for _ in range(rows)])
        
        # Input the elements of the second matrix row-wise
        print("Enter second matrix elements row-wise:")
        matrix2 = np.array([list(map(float, input().split())) for _ in range(rows)])
        
        # Perform the selected operation
        if choice == '1':  # Matrix addition
            return matrix1 + matrix2
        elif choice == '2':  # Matrix subtraction
            return matrix1 - matrix2
        elif choice == '3':  # Matrix multiplication
            return np.dot(matrix1, matrix2)
        elif choice == '4':  # Determinant of the first matrix
            return np.linalg.det(matrix1)
        else:  # Handle invalid input
            return "Invalid choice"
