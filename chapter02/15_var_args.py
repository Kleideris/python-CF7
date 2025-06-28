def print_cities(*cities):
    if not cities:
        print("No cities provided")
    else:
        print("Cities:", ", ".join(cities))
    pass

def main():
    print_cities()
    print_cities("Athens")
    print_cities("Athens", "London", "Paris")

if __name__ == "__main__":
    main()