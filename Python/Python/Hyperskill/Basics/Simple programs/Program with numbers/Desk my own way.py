classes = []
for count in range(1, 4):
    classes.append(int(input()))
total_desks = 0
for students in classes:
    desks, more_students = students // 2, students % 2
    total_desks += desks + (more_students != 0)
print(total_desks)
