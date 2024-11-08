# Student Grade Calculator

## Overview

The **Student Grade Calculator** is a Python script designed to help users input their courses and corresponding marks, and calculate the grade based on predefined grade boundaries. This script ensures valid input and handles edge cases, such as duplicate course names and invalid marks.

## Features

- **Dynamic Course Input**: Users can enter the names of their courses dynamically.
- **Input Validation**: Ensures that the marks entered are within the valid range (0-100) and that each course name is unique.
- **Grade Calculation**: Computes the grade based on the input marks using predefined grade boundaries.
- **User-Friendly Prompts**: Provides clear and informative prompts to guide the user through the input process.

## Usage

1. **Enter Course Names**: Start by entering the names of the courses you took. Type `'done'` when you have entered all your courses.
2. **Enter Marks**: For each course, enter your marks when prompted.
3. **Get Grades**: The script will calculate and display your grade for each course based on the marks entered.

## Grade Boundaries

| Grade | Marks Range |
|-------|-------------|
| A     | 70 - 100    |
| B     | 60 - 69     |
| C     | 50 - 59     |
| D     | 40 - 49     |
| E     | 30 - 39     |
| F     | 0 - 29      |

## Code Explanation

### Grade Boundaries
The grade boundaries are defined in a dictionary where each grade is associated with a range of marks:

```python
grade_boundaries = {
    'A': (70, 100),
    'B': (60, 69),
    'C': (50, 59),
    'D': (40, 49),
    'E': (30, 39),
    'F': (0, 29),
}
```

### Functions
**determine_grade(marks):**
This function determines the grade based on the marks provided. It iterates through the grade boundaries and returns the corresponding grade if the marks fall within the specified range.

```python
def determine_grade(marks):
    for grade, (low, high) in grade_boundaries.items():
        if low <= marks <= high:
            return grade
    return None
```
**get_subjects():**
This function prompts the user to enter the names of the courses they have taken. It continues to ask for course names until the user types 'done'. It also checks for empty inputs and duplicate course names.

``` python
def get_subjects():
    subjects = []
    while True:
        subject = input("Enter the name of a course (or 'done' to finish): ").strip()
        if subject.lower() == 'done':
            break
        if subject:  # Check if the input is not empty
            if subject in subjects:
                print(f'The course "{subject}" has already been entered. Please enter a different course.')
            else:
                subjects.append(subject)
        else:
            print("Please enter a valid course name.")
    return subjects
```
**main():**
The main function orchestrates the execution of the script. It first calls **get_subjects()** to get the list of subjects from the user. Then, it loops through each subject to get the marks, validates the input, and calculates the grade using **determine_grade(marks)**.

```python
def main():
    subjects = get_subjects()  # Get the list of subjects from the user
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

if __name__ == "__main__":
    main()
```

## Installation
To run this script, you'll need Python installed on your machine. Clone the repository and execute the script in your terminal:

```python
git clone https://github.com/yourusername/student-grade-calculator.git
cd student-grade-calculator
python grade_calculator.py
```
