num = 10
my_dict = {"count": 0}

def main():
    # num = 100
    num += 100  # Tha petaksei sfalma giati h num edeixne se primitive. #TODO na to ksanadw sto spiti!!
    print(num)
    print(my_dict)
    my_dict["count"] += 1
    print(my_dict)

if __name__ == "__main__":
    main()