import math
import numpy as np

class Matrix_operations:
    
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