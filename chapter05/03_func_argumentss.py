def test_args_func(pos_arg1, pos_arg2, opt_arg1=None, opt_arg2=None, *args, **kwargs):
    """
    Function to demostrate the usage of positional, optional, additional optional (*args) and additional keyword arguments (**kwargs).

    Parameters:
        pos_arg1 (Any): The first positional argument.
        pos_arg2: The second positional argument.
        opt_arg1: The first optional argument. Defaults to None.
        opt_arg2: The second optional argument. Defaults to None.
        *args: Additional positonal arguments.
        **kwargs: Additional keyword arguments.
    """
    # Print positional arguments
    print("Pos arg1:",pos_arg1)
    print("Pos arg2:",pos_arg2)

    # Print optional arguments
    print("Opt arg1:", opt_arg1)
    print("Opt arg2:", opt_arg2)

    # Print additional pos args
    if args:
        print("Additional pos args:")
        for arg in args:
            print(arg)

    if kwargs:
        print("Additional Keyword args:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

def main():
    # test_args_func()  # without possisional args this will raise an error!

    test_args_func("Hello", "CF7", 100, 200)
    print("-------------------")

    test_args_func("Hello", "CF7", arg2=100)
    print("-------------------")

    test_args_func(pos_arg2="Hello", pos_arg1="CF7", arg2=100)
    print("-------------------")

    test_args_func("Hello", "CF7", name="Chris", age=101)
    print("-------------------")

    test_args_func("Hello", "CF7", 12, 42, 52, "lala")
    print("-------------------")

    test_args_func("Hello", "CF7",                 # pos_arg1, pos_arg2
                    100, 200,                      # opt_args1, opt_args2
                    300, "Bob",                    # args
                    name="Chris", street="Coding"  # kwargs
                    )    
    print("-------------------")

if __name__ == "__main__":
    main()