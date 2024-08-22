# input enter less then 100

# Input subject names and marks
subject1 = input("Enter subject 1 name: ")
subject1_marks = int(input("Enter subject 1 marks obtained out of 100: "))

subject2 = input("Enter subject 2 name: ")
subject2_marks = int(input("Enter subject 2 marks obtained out of 100: "))

subject3 = input("Enter subject 3 name: ")
subject3_marks = int(input("Enter subject 3 marks obtained out of 100: "))

subject4 = input("Enter subject 4 name: ")
subject4_marks = int(input("Enter subject 4 marks obtained out of 100: "))

# Storing names and marks
subject_names = (subject1, subject2, subject3, subject4)
marks = (subject1_marks, subject2_marks, subject3_marks, subject4_marks)

# Validating marks
if any(mark > 100 or mark < 0 for mark in marks):
    print("Error: Marks should be between 0 and 100.")
else:
    # Calculate total and percentage
    total_marks = sum(marks)
    percentage = (total_marks / 400) * 100

    # Determine grade
    if percentage >= 90:
        grade = "A grade"
    elif percentage >= 80:
        grade = "B grade"
    elif percentage >= 70:
        grade = "C grade"
    elif percentage >= 60:
        grade = "D grade"
    else:
        grade = "F grade"

    # Determine pass/fail
    if grade == "F grade":
        pass_fail = "Fail"
    else:
        pass_fail = "Pass"

    # Print results
    print(grade)
    print(pass_fail)
    print(f"Total Marks: {total_marks}/400")
    print(f"Percentage: {percentage}%")
    # print(f"All Subjects Names: {subject_names}")
