grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students=sorted(students)
students_list = list(sorted_students)

if len(students_list) != len(grades):
    print("Количество студентов и групп оценок не совпадает.")
else:
    student_grades = {}
    for student, group in zip(students_list, grades):
        average = sum(group) / len(group)
        student_grades[student] = average

    for student, avg in student_grades.items():
        print(f"{student}: {avg:.2f}")


