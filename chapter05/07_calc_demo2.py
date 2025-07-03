import functools
# from functools import reduce

def calculate(args):
    def plus():
        """Return the sum of the numbers"""
        return functools.reduce(lambda x, y: x + y, args)
    
    def minus():
        """Returns the dif of the numbers"""
        return functools.reduce(lambda x, y: x - y, args)
    # [100, 10, 20, 30] -> 100 - 10 - 20 - 30
    
    def mul():
        """Returns the mul of the numbers"""

        return functools.reduce(lambda x, y: x * y, args)
    
    def div():
        """Returns the div of the numbers"""
        if not 0 in args[1:]:
            # return functools.reduce(lambda x, y: x / y, args)
            return args[0] / sum(args[1:])
    
    return {
        "add": plus,
        "subtract": minus,
        "multiply": mul,
        "division": div
    }

def main():
    list_of_ints = [26, 5, 4, 3, 2, 1]

    operations = calculate(list_of_ints)

    while True:
        print("\nChoose an operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. DivisExition")

        try:
            choice = int(input("Please enter a number between 1 and 5: "))
        except ValueError:
            print("Invalid input.")
            continue
        match choice:
            case 1:
                print("Addition:", operations["add"]())
            case 2:
                print("Subtraction:", operations["subtract"]())
            case 3:
                print("Multiplication:", operations["multiply"]())
            case 4:
                print("Division:", operations["division"]())
            case 5:
                print("Goodbye")
                break
            case _:
                print("Invalid input. Please try again")


    
    

if __name__ == "__main__":
    main()