def upscale_grades(grades):
    upscaled = [grade + 1 if grades <= 9 else grade for grade in grades] #TODO na to katanohsw
    return upscaled

def filter_passed(grades):
    passed = [grade for grade in grades if grade >= 5]

def categorise_grades(grades):
    passed = [grade for grade in grades if grade >= 5 and grade < 10]
    failed = [grade for grade in grades if grade < 5]
    honors = [grade for grade in grades if grade == 10]
    return passed, failed, honors

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def main():
    grades = [7, 5, 9, 10, 5, 3, 7, 8]  #TODO na to ylopoihsw me randint
   
    upscaled_grades = upscale_grades(grades)
    print(f"Initial grades: {grades}")
    print(f"Upscaled grades: {upscaled_grades}")

    passed_gd, failed_gd, honored_gd = calculate_average(grades=grades)

    print(f"Passed students: {passed_gd}")
    print(f"Failed students: {failed_gd}")
    print(f"Honored students: {honored_gd}")


if __name__ == "__main__":
    main()