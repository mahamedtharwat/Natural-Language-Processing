import re

# Regular expression pattern
pattern = r"\d{2}-\d{5}"

# Test string
student_id = "15-00041"

# Check if the string matches the pattern
if re.match(pattern, student_id):
    print("The student ID format is correct.")
else:
    print("The student ID format is incorrect.")
