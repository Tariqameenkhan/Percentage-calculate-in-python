# input enter less then 100

def get_marks(subject_name):
    while True:
        try:
            marks = int(input(f"Enter {subject_name} marks obtained (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Error: Marks must be between 0 and 100. Please enter a valid mark.")
        except ValueError:
            print("Error: Please enter a valid integer.")

def get_subject(subject_number):
    return input(f"Enter subject {subject_number} name: ")

# Collect subject names and marks
subject1 = get_subject(1)
subject1_marks = get_marks(subject1)

subject2 = get_subject(2)
subject2_marks = get_marks(subject2)

subject3 = get_subject(3)
subject3_marks = get_marks(subject3)

subject4 = get_subject(4)
subject4_marks = get_marks(subject4)

# Calculate total marks and percentage
total_marks = subject1_marks + subject2_marks + subject3_marks + subject4_marks
percentage = (total_marks / 400) * 100 

# Determine grade and pass/fail
if percentage >= 90:
    grade = "A"
    status = "pass"
elif percentage >= 80:
    grade = "B"
    status = "pass"
elif percentage >= 70:
    grade = "C"
    status = "pass"
elif percentage >= 60:
    grade = "D"
    status = "pass"
else:
    grade = "F"
    status = "Fail"

# Print results
print(f"Grade: {grade}")
print(f"Status: {status}")
print(f"Total Marks: {total_marks}/400")
print(f"Percentage: {percentage}%")
print(f"Subjects: {subject1}, {subject2}, {subject3}, {subject4}")
print(f"Marks Obtained: {subject1_marks}, {subject2_marks}, {subject3_marks}, {subject4_marks}")
