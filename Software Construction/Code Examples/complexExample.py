
def create_student_report(students_data):
    """
    Create a report from student data.    
    Args: students_data: List of dictionaries with student information
    Returns: dict: Summary report with statistics
    """
    report = {
        "total_students": len(students_data),
        "average_gpa": 0,
        "courses": {},
        "honor_students": []
    }
    
    total_gpa = 0
    for student in students_data:
        # Add to total GPA
        total_gpa += student["gpa"]
        # Track courses
        course = student["course"]
        if course not in report["courses"]:
            report["courses"][course] = 0
        report["courses"][course] += 1
        # Identify honor students (GPA >= 3.5)
        if student["gpa"] >= 3.5:
            report["honor_students"].append(student["name"])
    # Calculate average GPA
    if report["total_students"] > 0:
        report["average_gpa"] = total_gpa / report["total_students"]
    
    return report
# Sample data
students = [
    {"name": "Alice", "course": "CS", "gpa": 3.8},
    {"name": "Bob", "course": "Math", "gpa": 3.2},
    {"name": "Charlie", "course": "CS", "gpa": 3.9}
]
print(create_student_report(students))
