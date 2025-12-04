import sys

def Main_of_all():
    def easy_main():
        def rectangle_area():
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            if length < 0 or width < 0:
                print("Invalid input. Please enter numeric values.")
                return rectangle_area()
            area = length * width
            print(f"The area of the rectangle is: {area}")
            cont = input("Do you want to try again or go back to easy menu? (1. try again/2. back): ")
            if cont == "1":
                return rectangle_area()
            elif cont == "2":
                return easy_main()
            else:
                print("Thank you for participating in the assessment!")

        def pos_neg_zero():
            number = float(input("Enter a number: "))
            if number > 0:
                print("The number is Positive.")
            elif number < 0:
                print("The number is Negative.")
            else:
                print("The number is Zero.")
            cont = input("Do you want to try again or go back to easy menu? (1. try again/2. back): ")
            if cont == "1":
                return pos_neg_zero()
            elif cont == "2":
                return easy_main()
            else:
                print("Thank you for participating in the assessment!")

        def counting_loop():
            n = int(input("Enter a positive integer: "))
            if n < 0:
                print("Invalid input. Please enter a positive integer.")
                return counting_loop()
            print("Counting from 1 to", n)
            for i in range(1, n + 1):
                print(i)
            cont = input("Do you want to try again or go back to easy menu? (1. try again/2. back): ")
            if cont == "1":
                return counting_loop()
            elif cont == "2":
                return easy_main()
            else:
                print("Thank you for participating in the assessment!")

        def max_of_two():
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num1 > num2:
                print(f"The maximum number is: {num1}")
            else:
                print(f"The maximum number is: {num2}")
            cont = input("Do you want to try again or go back to easy menu? (1. try again/2. back): ")
            if cont == "1":
                return max_of_two()
            elif cont == "2":
                return easy_main()
            
        def sum_of_list():
            elements = input("Enter numbers separated by spaces: ")
            try:
                num_list = [float(x) for x in elements.split()]
                total = sum(num_list)
                print(f"The sum of the list elements is: {total}")
            except ValueError:
                print("Invalid input. Please enter numeric values only.")
                return sum_of_list()
            cont = input("Do you want to try again or go back to easy menu? (1. try again/2. back): ")
            if cont == "1":
                return sum_of_list()
            elif cont == "2":
                return easy_main()
            else:
                print("Thank you for participating in the assessment!")

        print("fundamental programming assessment for beginners" \
        "\n===============================================================" \
        "\npart 1 - Rectangle Area (Basics, Data Types, Input/Output)" \
        "\npart 2 - Positive, Negative, or Zero (Conditions)" \
        "\npart 3 - Counting with a Loop (Loops, Basics)" \
        "\npart 4 - Simple Function: Maximum of Two (Functions, Conditions)" \
        "\npart 5 - Sum of List Elements (Lists, Loop, Data Types)" \
        "\n6 - back to main menu" \
        "\n===============================================================")
        choice = input("choose one of the parts you want to test (use number 1,2,3,4,5,6 only): ")
        
        if choice == "1":
            return rectangle_area()
        elif choice == "2":
            return pos_neg_zero()
        elif choice == "3":
            return counting_loop()
        elif choice == "4":
            return max_of_two()
        elif choice == "5":
            return sum_of_list()
        elif choice == "6":
            return Main_of_all()
        else:
            print("Invalid choice. Please try again.")
            return easy_main()

    def moderate_main():
    
        def grade_classifier():

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
                cont = input("Do you want to try again or go back to easy menu? (1. try again/2. back): ")
                if cont == "1":
                    return grade_classifier()
                elif cont == "2":
                    return moderate_main()
                else:
                    print("Thank you for participating in the assessment!")
        
        def count_even_numbers():
            n = int(input("Enter a positive integer: "))
            if n < 0:
                print("Invalid input. Please enter a positive integer.")
                return count_even_numbers()
            print("Even numbers from 1 to", n)
            for i in range(2, n + 1, 2):
                print(i)
            cont = input("Do you want to try again or go back to easy menu? (1. try again/2. back): ")
            if cont == "1":
                return count_even_numbers()
            elif cont == "2":
                return moderate_main()
            else:
                print("Thank you for participating in the assessment!")

        def multiplication_table():
            while True:
                num = int(input("enter a number to see its multiplication table: "))
                for i in range(1, 11):
                    result = num * i
                    print(f"{num} x {i} = {result}")
                cont = input("Do you want to try again or go back to easy menu? (1. try again/2. back): ")
                if cont == "1":
                    return multiplication_table()
                elif cont == "2":
                    return moderate_main()
                else:
                    print("Thank you for participating in the assessment!")

        def Factorial_Function():
            def factorial(n):
                if n == 0 or n == 1:
                    return 1
                else:
                    return n * factorial(n - 1)

            while True:
                num = int(input("Enter a non-negative integer to compute its factorial: "))
                if num < 0:
                    print("Invalid input. Please enter a non-negative integer.")
                    continue
                print(f"The factorial of {num} is {factorial(num)}")
                cont = input("Do you want to try again or go back to easy menu? (1. try again/2. back): ")
                if cont == "1":
                    return Factorial_Function()
                elif cont == "2":
                    return moderate_main()
                else:
                    print("Thank you for participating in the assessment!")

        def list_of_names():

            def name_add():
                global students
                for i in range(3):
                    name = input(f"Enter student name #{i + 1}: ")
                    students.append(name)
                print("\nStudent list:")
                for student in students:
                    print(student)

            def remove_name():
                global students
                name_to_remove = input("\nEnter one name to remove: ")
                if name_to_remove in students:
                    students.remove(name_to_remove)
                    print("\nUpdated student list:")
                    for student in students:
                        print(student)
                else:
                    print("Name not found.")
            
            while True:
                
                print("\nMain Menu:")
                print("1. Add Student Names")
                print("2. Remove a Student Name")
                print("3. Exit")
                choice = input("Choose an option (1-3): ")
                if choice == "1":
                    name_add()
                elif choice == "2":
                    remove_name()
                elif choice == "3":
                    return moderate_main()
                else:
                    print("Invalid choice. Please try again.")
            

        print("fundamental programming assessment for beginners" \
        "\n===============================================================" \
        "\npart 1 - Grade Classifier (Conditions, Data Types)" \
        "\npart 2 - Count Even Numbers (Lists, Loops, Conditions) " \
        "\npart 3 - Multiplication Table (Loops, Basics) " \
        "\npart 4 - Factorial Function (Functions, Loops) " \
        "\npart 5 - Manage a List of Names (Lists, Functions, Loops)" \
        "\n6 - back to main menu" \
        "\n===============================================================")
        choice = input("choose one of the parts you want to test (use number 1,2,3,4,5,6 only): ")
        if choice == "1":
            return grade_classifier()
        elif choice == "2":
            return count_even_numbers()
        elif choice == "3":
            return multiplication_table()
        elif choice == "4":
            return Factorial_Function()
        elif choice == "5":
            return list_of_names()
        elif choice == "6" or choice.lower() == "back to main menu":
            return Main_of_all()
        else:
            print("Invalid choice. Please try again.")
            return moderate_main()

    def hard_main():

        def compute_stats():
            numbers = []

            print("Enter 5 integers:")

            for i in range(5):
                num = int(input(f"Enter integer #{i + 1}: "))
                numbers.append(num)

            smallest = min(numbers)
            largest = max(numbers)
            average = sum(numbers) / len(numbers)

            print("Smallest number:", smallest)
            print("Largest number:", largest)
            print("Average:", average)

            cont = input("Do you want to try again or go back to easy menu? (1. try again/2. back): ")
            if cont == "1":
                return compute_stats()
            elif cont == "2":
                return hard_main()
            else:
                print("Thank you for participating in the assessment!")

        def word_count():
            sentence = input("Enter a sentence: ")

            words = sentence.split()  # split on spaces
            counts = {}               # word -> count

            for word in words:
                word = word.lower()   # optional: ignore case
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

            print("\nWord counts:")
            for word, count in counts.items():
                print(f"{word}: {count}")
            cont = input("Do you want to try again or go back to easy menu? (1. try again/2. back): ")
            if cont == "1":
                return word_count()
            elif cont == "2":
                return hard_main()
            else:
                print("Thank you for participating in the assessment!")


        def score_analysis():
            scorelist = []
            
            num_scores = int(input("How many scores do you want to input? "))
            for i in range(num_scores):
                while True:
                    try:
                        score = float(input(f"Enter score {i + 1}: "))
                        if 0 <= score <= 100:
                            scorelist.append(score)
                            break
                        else:
                            print("Invalid score. Please enter a score between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
            highest_score = max(scorelist)
            lowest_score = min(scorelist)
            average_score = sum(scorelist) / len(scorelist)
            numberofpasses = len([s for s in scorelist if s >= 60])
            print("============================================")
            print("Score Analysis Report")
            print("============================================")
            print("Scores:", scorelist)
            print("highest score:",highest_score)
            print("lowest score:", lowest_score)
            print("average score:", average_score)
            print("number of passes:", numberofpasses)
            cont = input("Do you want to try again or go back to easy menu? (1. try again/2. back): ")
            if cont == "1":
                return score_analysis()
            elif cont == "2":
                return hard_main()
            else:
                print("Thank you for participating in the assessment!")
        
        def calculator():
            add = lambda x, y: x + y
            subtract = lambda x, y: x - y
            multiply = lambda x, y: x * y
            divide = lambda x, y: x / y if y != 0 else 'Error: Division by zero'
            modulo = lambda x, y: x % y if y != 0 else 'Error: Division by zero'

            calculate = lambda num1, num2, ope: (
                add(num1, num2) if ope == '+' else
                subtract(num1, num2) if ope == '-' else
                multiply(num1, num2) if ope == '*' else
                divide(num1, num2) if ope == '/' else
                modulo(num1, num2) if ope == '%' else
                'Error: Invalid operator'
            )

            while True:
                num1 = int(input('Enter #1: '))
                num2 = int(input('Enter #2: '))
                ope = input('Enter operator[+,-,/,*,%]: ')
                print(f'{num1} {ope} {num2} = {calculate(num1, num2, ope)}')
                cont = input("Do you want to try again or go back to easy menu? (1. try again/2. back): ")
                if cont == "1":
                    return calculator()
                elif cont == "2":
                    return hard_main()
                else:
                    print("Thank you for participating in the assessment!")

        def password_strength_checker():
            import re

            def check_password_strength(password):
                length = len(password)
                has_letter = re.search(r"[A-Za-z]", password) is not None
                has_digit = re.search(r"[0-9]", password) is not None
                only_letters = password.isalpha()


                if length >= 8 and has_letter and has_digit:
                    print("Strong")

                
                elif length >= 6 and only_letters:
                    print("Medium")

                
                else:
                    print("Weak")

            while True:
                password = input("Enter a password to check its strength: ")
                check_password_strength(password)

                cont = input("Do you want to try again or go back to hard menu? (1. try again/2. back): ")
                if cont == "1":
                    continue
                elif cont == "2":
                    return hard_main()
                else:
                    print("Thank you for participating in the assessment!")
                    return


        print("fundamental programming assessment for beginners" \
        "\n===============================================================" \
        "\npart 1 - Basic Statistics (Lists, Functions, Data Types)" \
        "\npart 2 - Word Frequency Counter (Lists, Loops, Data Types)" \
        "\npart 3 - Filter Passing Grades (Lists, Conditions, Functions)" \
        "\npart 4 - Simple Menu-Driven Calculator (Loops, Conditions, Functions)" \
        "\npart 5 -  Password Strength Checker (Conditions, Functions, Strings/Data Types)" \
        "\n6 - back to main menu" \
        "\n===============================================================")
        choice = input("choose one of the parts you want to test (use number 1,2,3,4,5,6 only): ")
        if choice == "1":
            return compute_stats()
        elif choice == "2":
            return word_count()
        elif choice == "3":
            return score_analysis()
        elif choice == "4":
            return calculator()
        elif choice == "5":
            return password_strength_checker()
        elif choice == "6" or choice.lower() == "back to main menu":
            return Main_of_all()
        else:
            print("Invalid choice. Please try again.")
            return hard_main()

    print("Welcome to the Python Assessments!" \
    "\n==================================================================" \
    "\nChoose the python assessment difficulty you want to take" \
    "\n==================================================================" \
    "\n1- easy" \
    "\n2- medium" \
    "\n3- hard" \
    "\n4- exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        easy_main()
    elif choice == "2":
        moderate_main()
    elif choice == "3":
        hard_main()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")

# list to hold
students = [] #for list_of_names function


# list to hold
students = []  # for list_of_names function

if __name__ == "__main__":
    Main_of_all()
