def main():
    students = {
    'Bob': 90,
    'Charlie': 94,
    'Diana': 80,
    'Eve': 81,
    'Alice': 85,
}
    
    # Find the student with the student name with lowest alphabetical value order.
    student_with_min_grade = min(students)  # TODO na dw an ginetai me trythy falsy (na dw kai pws legontai auta)
    print(student_with_min_grade)

    # Student with min grade!
    student_with_min_grade = min(students, key=students.get)
    print(student_with_min_grade)

    student_with_min_grade = min(students.values())  # ayto den tha doulepsei giati tha mou dwsei to idio to value oxi to name
    print(student_with_min_grade)



    # Student with the shortest name by length
    student_with_min_grade = min(students, key=len)
    print(student_with_min_grade)

if __name__ == "__main__":
    main()