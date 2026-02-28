# Student Grade Calculator

def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid Marks! Please enter marks between 0 and 100."

    if marks >= 90:
        return "Grade: A+"
    elif marks >= 80:
        return "Grade: A"
    elif marks >= 70:
        return "Grade: B"
    elif marks >= 60:
        return "Grade: C"
    elif marks >= 50:
        return "Grade: D"
    else:
        return "Grade: F"


# Taking input from user
try:
    marks = float(input("Enter your marks (0-100): "))
    result = calculate_grade(marks)
    print(result)
except ValueError:
    print("Invalid input! Please enter numeric value.")
