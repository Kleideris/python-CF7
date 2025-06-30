def compare_integers(a: int, b: int):
    if a == b:
        print("the numbers are equal.")
    elif a > b:
        print("the first number is greater than the second number.")
    else:
        print(" the first number is less than the second number.")

def main():
    try:
        a = int(input("Please enter the first number: "))
        b = int(input("Please enter the second number: "))
    except ValueError:
        print("Invalid input.")
        return
    
    compare_integers(a, b)
    
    # 1. simple exaple (ternary operator)
    if a > 0:
        print("positive")
    else:
        print("non-positive")

    result = "positive" if a > 0 else "non-positive"
    print(result)
    #nprint("positive" if a > 0 else "non-positive")

    # 2. extended example (ternary operator)
    result = (
        "the numbers are equal." if a == b else
        "the first number is greater than the second number." if a > b else
        "the first number is less than the second number."
    )
    
    print(result)

if __name__ == "__main__":
    main()