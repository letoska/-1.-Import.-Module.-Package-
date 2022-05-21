class Student:
    def __init__(self, name, surname, gender):
        self.courses_attached = []
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя = {self.name} Фамилия = {self.surname}'
        return res

        # Средняя
        # оценка
        # за
        # домашние
        # задания: 9.9
        # Курсы
        # в
        # процессе
        # изучения: Python, Git
        # Завершенные
        # курсы: Введение
        # в
        # программирование

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Reviewer(Mentor):
    def rate_s(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_s(best_student, 'Python', 10)
cool_mentor.rate_s(best_student, 'Python', 10)
cool_mentor.rate_s(best_student, 'Python', 10)

print(best_student.grades)

best_lecturer = Lecturer('Voldemar', 'Stanov', 'Man')
best_lecturer.courses_in_progress += ['Python']

cool_student = Student('Ruoy', 'Eman', 'Man')
cool_student.courses_attached += ['Python']

cool_student.rate_l(best_lecturer, 'Python', 10)
cool_student.rate_l(best_lecturer, 'Python', 10)
cool_student.rate_l(best_lecturer, 'Python', 10)

print(best_lecturer.grades)
print(123131)