def student_grade_system():
    students = {}
    while True:
        print("\nStudent Grade System")
        print("1. Add student")
        print("2. Add grade")
        print("3. Calculate average")
        print("4. Display all students")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            if name not in students:
                students[name] = []
                print(f"Student {name} added.")
            else:
                print("Student already exists.")
                
        elif choice == '2':
            name = input("Enter student name: ")
            if name in students:
                try:
                    grade = float(input("Enter grade: "))
                    students[name].append(grade)
                    print(f"Grade {grade} added for {name}.")
                except ValueError:
                    print("Invalid grade. Please enter a number.")
            else:
                print("Student not found.")
                
        elif choice == '3':
            name = input("Enter student name: ")
            if name in students:
                grades = students[name]
                if grades:
                    average = sum(grades) / len(grades)
                    print(f"Average grade for {name}: {average:.2f}")
                else:
                    print(f"No grades recorded for {name}.")
            else:
                print("Student not found.")
        
        elif choice == '4':
            if students:
                for name, grades in students.items():
                    if grades:
                        print(f"{name}: {grades} (Avg: {sum(grades)/len(grades):.2f})")
                    else:
                        print(f"{name}: No grades recorded")
            else:
                print("No students in the system.")
                
        elif choice == '5':
            print("Exiting system.")
            break
            
        else:
            print("Invalid choice. Please try again.")

# Run the system
student_grade_system()
