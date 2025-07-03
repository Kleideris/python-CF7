def department_id_generated(department):
    last_id = 0

    def generate_id():
        nonlocal last_id
        last_id += 1
        return f"{department}-{last_id}", last_id
    
    return generate_id

def main():
    python_id_gen = department_id_generated("Python")
    android_id_gen = department_id_generated("Android")

    print(python_id_gen())
    print(python_id_gen())

    print(android_id_gen())
    print(android_id_gen())

if __name__ == "__main__":
    main()