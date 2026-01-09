def greeting(name):
    return "Hello {}!".format(name)

def message(student):
    filled_in_message="""
    Hi {}!
    This is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {} and can increase to {} if you submit all assignments before the due date.
    """.format(student['name'], student['missing_assignment_amount'], student['current_grade'], student['potential_grade'])
    return filled_in_message




# user_name = input("Enter thy name, teacher: ")
# print(greeting(user_name))

student_data = [
    {'name': "Dave", 'missing_assignment_amount': 2, 'current_grade': 7, 'potential_grade': 8},
    {'name': "Jane", 'missing_assignment_amount': 13, 'current_grade': 4, 'potential_grade': 7.5},
]

for student in student_data:
    print(message(student) + '\n')