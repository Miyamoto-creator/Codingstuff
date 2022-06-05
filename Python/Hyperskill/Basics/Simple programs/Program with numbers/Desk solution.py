def get_student_nums(num_classes=3):

    classes = []  # empty list to store the three class sizes
    for count in range(1, num_classes + 1):  # so count has value 1, then 2, ... to num_count

        while True:  # input validation
            try:  # to trap bad input that will not convert to integer
                students = int(input(f'Number of students in class {count}: '))
                if 1 <= students <= 1000:  # check for sensible number
                    break  # leave while loop, input is valid
            except ValueError:  # int conversion failed
                pass  # don't do anything here, next line will also cover poor value
            print('Expecting a number between 1 and 1000 inclusive')

        classes.append(students)  # got here after breaking from while loop

    return classes

def calc_desks(classes, num_per_desk=2):

    total_desks = 0
    for students in classes:
        # desks, more_students = divmod(students, num_per_desk)  # integer division and remainder OR
        desks, more_students = students // num_per_desk, students % num_per_desk
        total_desks += desks + (more_students != 0)  # adds 1 if more students is not 0
    return total_desks


student_nums = get_student_nums()
num_of_desks = calc_desks(student_nums)
print(f'For {sum(student_nums)} students in three classes need {num_of_desks} desks')
