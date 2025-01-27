import random
import pyfiglet
import math
import Matrix_Operations as MO

class ScientificCalculator:
    #  ANSI color codes 
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    
    # List of random facts to display when the calculator starts
    random_facts = (
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.", 
        "Bananas are berries, but strawberries aren't.", 
        "A flock of flamingos is called a 'flamboyance.'", 
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.", 
        "Humans share 60% of their DNA with bananas.", 
        "There are more stars in the universe than grains of sand on all the Earth's beaches.", 
        "A day on Venus is longer than a year on Earth.", 
        "Octopuses have three hearts. Two pump blood to the gills, while one pumps it to the rest of the body.", 
        "A group of owls is called a 'parliament.'", 
        "The Eiffel Tower can be 15 cm taller during the summer because of the expansion of iron in the heat."
    )

    def __init__(self):
        # Display a welcome message with colors and ASCII art
        print(f"{self.CYAN}Welcome{self.END} to the Scientific Side of the Calculator")
        print("\nWhat you want to do today")
        print(r"""
                               ._ o o
                               \_`-)|_
                            ,""       \ 
                          ,"  ## |   ಠ ಠ. 
                        ," ##   ,-\__    `.
                      ,"       /     `--._;)
                    ,"     ## /
                  ,"   ##    /
            """)
        ascii_art = pyfiglet.figlet_format("SCIENTIFIC")
        print(self.LIGHT_GREEN, ascii_art, self.END)
        
        # Display a random fact
        print(self.random_facts[int(random.random() * 10)])
        print("\n")
        
        # Continuously run the calculator
        while(True):
          self.runner()

    def runner(self):
        # Display menu options to the user
        print("\nChoose from the following options:")
        print("1. sin  2. cos  3. tan  4. csc  5. sec  6. cot")
        print("7. arcsin  8. arccos  9. arctan")
        print("10. sinh  11. cosh  12. tanh")
        print("13. Matrix Operations")
        print("or Enter a BODMAS equation")
        print("To close the calculator, enter 'EX'")
        x = input("Enter your choice: ")

        try:
            if x == '1':  # sin
                print(f"sin: {math.sin(math.radians(float(input('Enter angle in degrees: '))))}")

            elif x == '2':  # cos
                print(f"cos: {math.cos(math.radians(float(input('Enter angle in degrees: '))))}")

            elif x == '3':  # tan
                print(f"tan: {math.tan(math.radians(float(input('Enter angle in degrees: '))))}")

            elif x == '4':  # cosec
                angle = math.radians(float(input('Enter angle in degrees: ')))
                print(f"csc: {1 / math.sin(angle) if math.sin(angle) != 0 else 'Undefined'}")

            elif x == '5':  # sec
                angle = math.radians(float(input('Enter angle in degrees: ')))
                print(f"sec: {1 / math.cos(angle) if math.cos(angle) != 0 else 'Undefined'}")

            elif x == '6':  # cot
                angle = math.radians(float(input('Enter angle in degrees: ')))
                print(f"cot: {1 / math.tan(angle) if math.tan(angle) != 0 else 'Undefined'}")

            elif x == '7':  # Arcsin
                value = float(input('Enter value between -1 and 1: '))
                print(f"arcsin: {math.degrees(math.asin(value))}")

            elif x == '8':  # Arccos
                value = float(input('Enter value between -1 and 1: '))
                print(f"arccos: {math.degrees(math.acos(value))}")

            elif x == '9':  # Arctan
                value = float(input('Enter value: '))
                print(f"arctan: {math.degrees(math.atan(value))}")

            elif x == '10':  # Hyperbolic sine
                value = float(input('Enter value: '))
                print(f"sinh: {math.sinh(value)}")

            elif x == '11':  # Hyperbolic cosine
                value = float(input('Enter value: '))
                print(f"cosh: {math.cosh(value)}")

            elif x == '12':  # Hyperbolic tangent
                value = float(input('Enter value: '))
                print(f"tanh: {math.tanh(value)}")

            elif x == '13':  # Matrix
                print(MO.Matrix_operations.matrix_operations())

            elif x.upper() == 'EX':  # Exit
                ascii_art = pyfiglet.figlet_format("BYE")
                print(self.LIGHT_GREEN, ascii_art, self.END)
                exit()

            else: # BODMAS equation
                print(f"Result: {eval(x)}")

        except Exception as e:
            print(f"Error: {e}")
        
