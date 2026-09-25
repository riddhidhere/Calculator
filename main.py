# --- Our GKS-U Project: Student GPA & Grade Calculator ---

print("=== Welcome to the Student Grade Calculator ===")

# 1. Asking the user to input their marks
physics = float(input("Enter your Physics marks (out of 100): "))
chemistry = float(input("Enter your Chemistry marks (out of 100): "))
maths = float(input("Enter your Mathematics marks (out of 100): "))

# 2. Calculating the Average Percentage
total_marks = physics + chemistry + maths
percentage = total_marks / 3

# 4.0 GPA Conversion Logic
if percentage >= 90:
    gpa = 4.0
elif percentage >= 80:
    gpa = 3.5
elif percentage >= 70:
    gpa = 3.0
elif percentage >= 60:
    gpa = 2.5
else:
    gpa = 2.0

print("\n--- YOUR RESULTS ---")
print(f"Your Overall Percentage is: {percentage:.2f}%")
print(f"Your Calculated GPA is: {gpa:.2f} / 4.0")

# 3. Computer decision block: Checking GKS-U Eligibility (80% cut-off)
if percentage >= 80:
    print("Status: Congratulations! You meet the GKS-U academic cut-off.")
    print("Grade: Distinction (Excellent Engineering Profile!)")
elif percentage >= 60:
    print("Status: You have a good score, keep pushing to cross the 80% mark!")
    print("Grade: First Class")
else:
    print("Status: Focus on strengthening your core concepts.")
    print("Grade: Clear")
