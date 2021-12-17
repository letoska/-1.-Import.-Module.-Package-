class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average()} ' \
              f'\nКурсы в процессе изучения: {"".join(self.courses_in_progress)} \nЗавершенные курсы: {"".join(self.finished_courses)}'
        return res

    def average(self):
        for x in self.grades.values():
            list_grades = x
        ave = sum(list_grades) / len(list_grades)
        return ave

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.average() < other.average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Lecturer(Mentor):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average()} '
        return res

    def average(self):
        global list_grades
        for x in self.grades.values():
            list_grades = x
        ave = sum(list_grades) / len(list_grades)
        return ave


class Reviewer(Mentor):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []

    def rate_s(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('John', 'Travolta', 'Man')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

cool_mentor = Reviewer('Revi', 'Ewer', 'Woman')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_s(best_student, 'Python', 9)
cool_mentor.rate_s(best_student, 'Python', 8)
cool_mentor.rate_s(best_student, 'Python', 7)

bad_student = Student('Steven', 'Sigal', 'Man')
bad_student.courses_in_progress += ['Python']
bad_student.finished_courses += ['Введение в программирование']
cool_mentor.rate_s(bad_student, 'Python', 6)
cool_mentor.rate_s(bad_student, 'Python', 6)
cool_mentor.rate_s(bad_student, 'Python', 6)

best_lecturer = Lecturer('Voldemar', 'Staropramen', 'Man')
best_lecturer.courses_in_progress += ['Python']
best_student.rate_l(best_lecturer, 'Python', 6)
best_student.rate_l(best_lecturer, 'Python', 5)
best_student.rate_l(best_lecturer, 'Python', 4)

bad_lecturer = Lecturer('Hannibal', 'Lecter', 'Man')
bad_lecturer.courses_in_progress += ['Python']
best_student.rate_l(bad_lecturer, 'Python', 4)
best_student.rate_l(bad_lecturer, 'Python', 4)
best_student.rate_l(bad_lecturer, 'Python', 4)

print(best_student)
print()
print(bad_student)
print()
print(best_lecturer)
print()
print(bad_lecturer)
print()

all_average_P = 0
all_average_G = 0
if best_student.courses_in_progress == ['Python']:
    all_average_P += best_student.average()
else:
    all_average_G += best_student.average()
if bad_student.courses_in_progress == ['Python']:
    all_average_P += bad_student.average()
else:
    all_average_G += bad_student.average()


# def average_grades(Student, course_name):
#     student1 = 'Ruoy'
#     student2 = 'Eman'
#     student3 = 'your_gender'
#     course_name = 'Python'
#     list_student = [student1, student2, student3]
#     for student in list_student:
#       if course_name == 'Python':
#         so = sum(student)
#         print(so)
# # print(best_student.average_grades)
# def averege_grades(courses_in_progress, Students):
#     for courses_in_progress, Students in best_student.items():
#         if courses_in_progress == 'Python':
#             print(sum(best_student.values()))
#             print(sum(Students))
# averege_grades('Python', Students)