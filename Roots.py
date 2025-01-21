# from argparse import  Namespace  # Importing the Namespace class from the argparse module to store variables.
from math import sqrt # Importing the sqrt function from the math module to calculate square roots

def roots (a, b, c):
    temp = (b*b) - 4*a*c  # Calculate the discriminant (b^2 - 4ac).

    if temp < 0:  # If the discriminant is negative, the roots are imaginary.
        print("Roots are Imaginary")

    elif temp == 0:  # If the discriminant is zero, there is one unique root.
        print("Root is Unique")
        print(f"Root is {-b/(2*a)}")

    elif temp > 0:  # If the discriminant is positive, the roots are real and different.
        print("Root is Diffrent")
        print(f" Roots are: {(-b-(sqrt(temp) ) ) / (2*a) } and {(-b+(sqrt(temp) ) ) / (2*a) }")
