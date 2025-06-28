def say_hello(name: str = "Coding Factory"):
    """
    Print a greeting message.

    Args:
        name (str): The name to greet. Default value 'Coding Factory'
    """
    print(f"Hello {name}")

def main():
    # say_hello(10)
    say_hello("Chris")
    say_hello()

    # print(say_hello.__doc__)
    help(say_hello)

    pass

if __name__ == "__main__":
    main()

