from argparse import ArgumentParser , Namespace
# Importing ArgumentParser and Namespace from the argparse module to handle command-line arguments.

import Roots, ScientificCalculator
# Importing custom modules Roots and ScientificCalculator for additional functionalities.

parser = ArgumentParser() # Creating an ArgumentParser object to parse command-line arguments.

parser.add_argument("X", type = int, nargs='?', help= "Value of X" )  # Adding a argument with an optional presence (`nargs='?'`) and a help message. parser.add_argument("Y", type = int, nargs='?', help= "Value of Y" )   Adding another positional argument 'Y', similar to 'X'.
parser.add_argument("Z", type = int, nargs='?', help= "Used when Calculating Roots", default = 0)  # Adding another argument, similar to 'X'.
parser.add_argument("-a", "--addition", help="It will Add the Value you entered", action="store_true")  
parser.add_argument("-s", "--substraction", help="It will Substract the Value you entered", action="store_true")
parser.add_argument("-m", "--multiplication", help="It will multiple the Value you entered", action="store_true")
parser.add_argument("-d", "--division", help="It will divide the Value you entered", action="store_true")
parser.add_argument("-p", "--percentage", help="It will calculate the Y percentage of X ", action="store_true")
parser.add_argument("-r", "--roots", help="It will caluculate the roots of the given Xx^2 + Yx + Z = 0 ", action="store_true")
parser.add_argument("-S", "--scientific", help="It will Switch to Scientific Calculator", action="store_true")


args: Namespace = parser.parse_args()   # Parsing the command-line arguments and storing them in the `args` variable.

# Below are the conditional checks for each flag and their respective functionalities.

if args.addition:
    print(f"Addition :{args.X + args.Y}")
    
if args.substraction:
    print(f"Substraction :{args.X - args.Y}")

if args.multiplication:
    print(f"Multiplication :{args.X * args.Y}")

if args.division:
    print(f"Division :{args.X / args.Y}")

if args.percentage:
    print(f"{args.Y}% Percentage of {args.X} is {args.X * (args.Y / 100)}")

if (args.roots or args.Z > 0):
    Roots.roots(args.X, args.Y, args.Z)

if args.scientific:
    ScientificCalculator.ScientificCalculator()









