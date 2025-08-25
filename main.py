# smart student Evalution system with python
#list of the sutdents who fails often in exams
s_fails_rol_no = ['BS02','BS06','BS10','BS24','BS32']
# sample student data
students_data =[
    {
        'name': 'Muntazer',
        'roll': 'BS72',
        'marks': {
            'Math': 90,
            'English': 85,
            'Science': 89
        }
    },
    {
        'name': 'Mavedat',
        'roll': 'BS68',
        'marks': {
            'Math': 70,
            'English': 65,
            'Science': 55
        }
    },
    
    {
        'name': 'Maryam',
        'roll': 'BS02',
        'marks': {
            'Math': 70,
            'English': 30,
            'Science': 28
        }
    }
]
# functions to calculate total ,average ,grade and check status
def evaulate_student(student):
    marks = student['marks']
    total = sum(marks.values())
    average = total / len(marks)
    
    # Pass or fail (must pass all subjects)
    passed = all(mark>= 35 for mark in marks.values())
    
    # Grading calculation
    if average >= 90:
        grade = 'A+'
    elif average >= 80:
        grade = 'A'
    elif average >=70:
        grade = 'B'
    elif average >=60:
        grade = 'C'
    else:
        grade = 'F'

    # Topper check
    is_topper = average >=85

    # check roll number validation
    roll = student['roll']
    valid_roll = roll.startswith('BS') and roll[2:].isdigit() and len(roll) == 4

    # frequent fail check
    frequent_fail = roll in s_fails_rol_no

    # Display student evaluation
    print(f"Student: {student['name']} | Roll No: {roll}")
    print(f"Marks: {marks}")
    print(f"Total: {total}, Average: {average:.2f}")
    print(f"Result: { 'Pass' if passed else 'Fail'}")
    print(f"Grade: {grade}")
    if is_topper:
        print("Status: Toppper! Congratulations!")
    if frequent_fail:
        print("Status: Frequent Fail - Needs Improvement")    
    if not valid_roll:
        print("Warning: Invalid Roll Number ")
# Ask for Roll number and show data only for the roll number
roll_no = input("Enter the roll number of the student (e.g., BS72): ").strip().upper()
found = False
for student in students_data:
    if student['roll'] ==roll_no:
        evaulate_student(student)
        found = True
        break
    if not found:
        print("Student with this roll number not found.")
            