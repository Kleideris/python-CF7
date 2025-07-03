from collections import deque

def display_garage(garage: deque) -> None:
    if garage:
        print("Current cars in the garage:")
        for i, car in enumerate(garage, 1):
            print(f"{i}. {car}")
    else:
        print("The garage is empty")

def add_car_to_garage(garage: deque, max_capacity: int) -> None:
    if len(garage) < max_capacity:
        car_name = input("Enter the name or ID of the car: ")
        garage.appent(car_name)
        print(f"{car_name} has entered in the garage.")
    else:
        print("The garage is full. Cannot add more cars.")

def remove_car_from_garage(garage: deque) -> None:
    if garage:
        car_left = garage.popleft()
        print(f"{car_left} has left the garage.")
    else:
        print("Garage is empty. No cars to remove.")

def main():
    #TODO: menu, printmenu, match, while true, testing.
    #TODO: na to kanw na afairei to amaksi pou thelw. me dict extra: na mporww na kalesw to amaksi kai apo th thesi kai apo thn pinakida (logika tha xrhsimpoeisw to idio dict kai tha to kalw diaforetika)!
    pass

if __name__ == "__main__":
    main()