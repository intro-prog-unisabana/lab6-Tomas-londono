def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}

def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}
    name = input("Enter student name:\n").strip().title()
    subjects = {}
    while True:
        entry = input("Enter subject and grade (or 'exit' to finish):\n").strip()
        if entry.lower() == "exit":
            break

        subject, grade = entry.split(",")
        subject = subject.strip().title()
        grade = float(grade.strip())
        subjects[subject] = grade
    student_grades[name] = subjects
    print(f"Student {name} successfully added to the grades management system.")
    return student_grades

def get_students(student_grades, keys):
    result = {}
    for name in keys:
        name_title = name.strip().title()
        found = False
        for student in student_grades:
            if student.lower() == name_title.lower():
                result[student] = student_grades[student]
                found = True
                break
        if not found:
            print(f"{name_title} not found!")
    return result

def avg_by_student(student_grades, keys=None):
    if keys is None:
        selected = student_grades
    else:
        selected = get_students(student_grades, keys)
    for student, grades in selected.items():
        if grades:
            avg = sum(grades.values()) / len(grades)
            print(f"{student}: {avg:.1f}")