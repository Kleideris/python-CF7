def facto():
    n, result = 0, 1
    while True:
        yield result
        n += 1
        result *= n

def main():
    f = facto()

    for i in range(6):
        print(f"{i}! = {next(f)}")

    for i in range(6, 11):  # edw to grapsame etsi gia na ektypwthei swsta sthn print to factorial.. Na to ksanadw
        print(f"{i}! = {next(f)}")
    
    print(f"{i + 1}! = {next(f)}")

if __name__ == "__main__":
    main()