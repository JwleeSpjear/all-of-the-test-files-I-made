grades = []

while True:
    grade = input("Enter your grade (or type 'exit' to finish): ")
    if grade.lower() == 'exit':
        break
    try:
        grade = float(grade)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    def get_grade(grade):
        scale = [
            (0, 59.9, "0.0"),
            (60, 63.9, "1.0"),
            (64, 67.9, "1.25"),
            (68, 70.9, "1.5"),
            (71, 73.9, "1.75"),
            (74, 76.9, "2.0"),
            (77, 79.9, "2.25"),
            (80, 82.9, "2.50"),
            (83, 85.9, "2.75"),
            (86, 88.9, "3.00"),
            (89, 91.9, "3.25"),
            (92, 94.9, "3.50"),
            (95, 97.9, "3.75"),
            (98, 100, "4.0"),
        ]
        for lower, upper, letter in scale:
            if lower <= grade <= upper:
                return letter
        return "Invalid grade"
    print(f"your grade is {get_grade(grade)}")