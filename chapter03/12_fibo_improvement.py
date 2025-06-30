def fibonacci():
    if n == 0: return 0
    if n == 1: return 1
    #if n in (0,1): return n

    #if 0 < n < 2 return n    TODO: na to dw sto spiti pws
    

    # a = 0
    # b = 0
    a, b = 0, 1



    for _ in range(2, n + 1):
        # temp = a
        # a = b
        # b = temp + b
        a, b = b, a + b  # first the values on the right are calculated, then they are assigned!

        return b

def main():
    pass

if __name__ == "__main__":
    main()