# List of subjects
subjects = ['Maths', 'Philosophy', 'Geography', 'Music']

# Dictionary with grade boundaries
grade_boundaries = {
    'A': (70, 100),
    'B': (60, 69),
    'C': (50, 59),
    'D': (40, 49),
    'E': (30, 39),
    'F': (0, 29),
}


# Function to determine grade based on marks
def determine_grade(marks):
    for grade, (low, high) in grade_boundaries.items():
        if low <= marks <= high:
            return grade
    return None


# Loop through each subject and get the user's marks
for subject in subjects:
    while True:  # Loop until valid input is received
        marks = input(f'Enter your marks for {subject}: ').strip()  # Add a space after the subject for clarity
        try:
            marks = int(marks)
            if marks < 0 or marks > 100:  # Check if marks are within the valid range
                print(f'Marks should be between 0 and 100. Please enter a valid number for {subject}.')
                continue
            grade = determine_grade(marks)
            if grade:
                print(f'Your grade for {subject} is: {grade}')
            else:
                print(f'Invalid marks for {subject}')
            break  # Exit the loop if input is valid and within range
        except ValueError:
            print(f'Invalid input for {subject}. Please enter a number.')

