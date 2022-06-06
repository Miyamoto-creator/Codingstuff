

class1 = abs(float(input()))
class2 = abs(float(input()))
class3 = abs(float(input()))

class1_total = abs(float(class1 // 2))
class2_total = abs(float(class2 // 2))
class3_total = abs(float(class3 // 2))

class1_round = abs(float(class1_total % 2))
class2_round = abs(float(class2_total % 2))
class3_round = abs(float(class3_total % 2))

class_round = class1_round + class2_round + class3_round
class_total = class1_total + class2_total + class3_total

total_desks = 0
classes = [3]

class1_final = abs(float(class1_total + class1_round))
class2_final = abs(float(class2_total + class2_round))
class3_final = abs(float(class3_total + class3_round))

def calc_desks(classes, num_per_desk=2):
    total_desks = 0
    for students in classes:
        # desks, more_students = divmod(students, num_per_desk)  # integer division and remainder OR
        desks, more_students = students // num_per_desk, students % num_per_desk
        total_desks += desks + (more_students != 0)  # adds 1 if more students is not 0
    return total_desks
class_final = class1_final + class2_final + class3_final
print(class_final)
print(class1_final)
print(class2_final)
print(class3_final)
print(class_round)
print(class_total)
print(total_desks)
