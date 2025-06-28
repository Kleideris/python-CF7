import re

# initialize my stack
stack = []

num = 0

def push(list, item):
    list.append(item)

def pop(list):
    if list:
        return list.pop()
    else:
        print("Stack is empty")
    
def print_stack(list):
    if list:
        print("Current state:", list)
    else:
        print("Stack is empty")

def print_menu():
    print("1. Insert on top")
    print("2. Get from top")
    print("3. Print Stack")
    print("4. q\Q for Quit")

def get_choice():
    return input("Please provide your choice\n")

def main():
    choice = 0
    num = 0
    out_num = 0

    while True:
        choice = get_choice()

        if not choice:
            continue

        if choice == 'q' or choice == 'Q':
            break

        pattern = r'^\d$'
        valid = re.match(pattern, choice)

        if not valid:
            print("Error in choice")
            continue

        choice = int(choice)

        match choice:
            case 1:
                num = input("Please insert a number: ")
                pattern = r'^\d+$'
                valid = re.match(pattern, num)
                if not valid:
                    print("Error in number")
                    continue

                num = int(num)
                #push on stack
                push(stack, num)
                print(f"{num} inserted.")

            case 2:
                out_num = pop(stack)
                if out_num is not None:
                    print("Item pop: ", out_num)
            
            case 3:
                print_stack(stack)
            
            case _:
                print("Not valid choice")





if __name__ == "__main__":
    main()