from collections import deque
#TODO add enumerate and the ability to choose if you take out a car by plate or by number.
def display_garage(garage: dict[str, str]) -> None:
    if garage:
        print("Current cars in the garage:")
        for plate, car in garage.items():
            print(f"Plate: {plate} — Car: {car}")
    else:
        print("The garage is empty")

def add_car_to_garage(garage: dict[str, str], max_capacity: int) -> None:
    if len(garage) >= max_capacity:
        print("The garage is full. Cannot add more cars.")

    user_input = input("Enter the car's plate and the name seperated by coma (ex: ABC123, Toyota Corolla): ")

    try:
        plate, car_name = map(str.strip, user_input.split(","))
    except ValueError:
        print("Invalid format. Please enter the plate and car name separated by a comma.")

    if not plate or not car_name:
         print("Both plate and name are required.")
    
    if plate in garage:
        print(f"Plate {plate} already exists.")
        return

    garage[plate] = car_name
    print(f"{car_name} with plate {plate} has been added.")
   
def remove_car_from_garage(garage: dict[str, str], plate: str) -> None:
    if not garage:
        print("Garage is empty. No cars to remove.")
        return
    if plate in garage:
        car_left = garage.pop(plate)
        print(f"{car_left} with plate {plate} has left the garage.")
    else:
        print(f"There are no cars in the garage with plate '{plate}'.")        

def main():
    garage = {"XXX123": "toyota", "YYY456": "mini cooper"}
    max_capacity = 100

    while True:
        print("\nChoose an operation:")
        print("1. Display garage")
        print("2. Add a car to the garage")
        print("3. Remove a car from the garage")
        print("4. Exit")

        try:
            choice = int(input("Please choose an option number 1 and 4: "))
        except ValueError:
            print("Invalid input.")
            continue
        
        match choice:
            case 1:
                display_garage(garage)
            case 2:
                add_car_to_garage(garage, max_capacity)
            case 3:
                plate = input("Enter the plate of the car you want to remove: ").strip()
                remove_car_from_garage(garage, plate)
            case 4:
                print("Goodbye")
                break
            case _:
                print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()