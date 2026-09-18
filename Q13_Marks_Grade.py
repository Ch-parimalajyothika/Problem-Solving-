def calculate_grade(marks):
    percentage = sum(marks) / 5
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"
    return percentage, grade

subjects = ["Physics", "Chemistry", "Biology", "Mathematics", "Computer"]
marks = [float(input(f"Enter {s} marks: ")) for s in subjects]
percentage, grade = calculate_grade(marks)
print("Percentage =", percentage)
print("Grade =", grade)
