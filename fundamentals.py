# Task 1: Data Science Fundamentals Assessment

# 1. Variables & Data Types
student_name = "Om"
skills = ["Python", "SQL", "Pandas", "Data Analysis"]
numbers = [10, 20, 30, 40, 50]

print("Student:", student_name)
print("Skills:", skills)

# 2. Basic Statistics Calculation (Mean)
mean_val = sum(numbers) / len(numbers)
print("Calculated Mean:", mean_val)

# 3. Simple Function
def analyze_score(score):
    if score >= 75:
        return "Distinction"
    else:
        return "Pass"

print("Result for 85:", analyze_score(85))
