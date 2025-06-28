def get_average(*numbers):
    """
    Calculates the average of multiple numbers.

    Parameters:
        *numbers (float or int): A variable number of numeric arguments.

    Returns:
        str: The average of the numbers formatted to two decimal places.
             If no numbers are provided, returns a message indicating that.
    """
    if not numbers:
        return "No numbers provided."
    
    average = sum(numbers) / len(numbers)
    return "{:.2f}".format(average)


def main():
    nums = [10, 20, 30, 40]

    my_average = get_average(*nums)
    my_average = get_average(10, 20, 30, 40)

    print(my_average)

if __name__ == "__main__":
    main()