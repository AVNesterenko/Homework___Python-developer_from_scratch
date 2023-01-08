
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades_student = {}
    
    def assessment_for_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in self.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def list_student(self, student):
        list_student = []
        if isinstance(student, Student):
            list_student += [student]
        else:
            list_student = [student]
        return

        for students in Student:
            if student in students:
                list_student += student
                print(list_student)
            else:
                print('Это не студент')
        return

    def student_average_grade(self):
        list_grade = []
        for key, value in self.grades_student.items():
            for grade in value:
                list_grade.append(grade)
        student_average_grade = round(sum(list_grade) / len(list_grade), 3)
        return student_average_grade
      
    def __str__(self):
        res = f"Имя: {self.name}" \
              f"\nФамилия: {self.surname}" \
              f"\nСредняя оценка за домашние задания: {self.student_average_grade()}" \
              f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}" \
              f"\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Данный студент в списке отсутствует!')
            return
        return self.student_average_grade() > other.student_average_grade()  
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_lecturer = {}

class Lecturer(Mentor):
    def lecturer_average_grade(self):
        list_grade_lecturer = []
        for key, value in self.grades_lecturer.items():
            for grade in value:
                list_grade_lecturer.append(grade)
        lecturer_average_grade = round(sum(list_grade_lecturer) / len(list_grade_lecturer), 3)
        return lecturer_average_grade

    def __str__(self):
        res = f"Имя: {self.name}" \
              f"\nФамилия: {self.surname}" \
              f"\nСредняя оценка за лекции: {self.lecturer_average_grade()}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Даннный лектор в списке отсутствует!')
            return
        return self.lecturer_average_grade() < other.lecturer_average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}' \
              f'\nФамилия: {self.surname}'
        return res

def average_grade_on_course_student(course, *list_student):
    '''
    Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
    '''
    list_grade = []
    for student in list_student:
        if student.grades_student.get(course):
            list_grade.extend(student.grades_student[course])
    return round(sum(list_grade) / len(list_grade), 3)

def average_grade_on_course_lectures(course, *list_lectures):
    """
    Подсчитываем среднюю оценку всех лекторов в рамках конкретного курса"""
    list_st = []
    for lecturer in list_lectures:
        if lecturer.grades_lecturer.get(course):
            list_st.extend(lecturer.grades_lecturer.get(course))
    return round(sum(list_st) / len(list_st), 1)

ivana_ivanova = Student('Ivana', 'Ivanova','female')
ivana_ivanova.finished_courses += ['Введение в программирование']
ivana_ivanova.courses_in_progress += ['Python', 'Git']
ivana_ivanova.courses_attached = ['Python', 'Git']

ivan_ivanov = Student('Ivan', 'Ivanov', 'male')
ivan_ivanov.finished_courses += ['Введение в программирование']
ivan_ivanov.courses_in_progress += ['Python', 'Git']
ivan_ivanov.courses_attached = ['Python', 'Git']


fedor_fedorov = Lecturer('Fedor', 'Fedorov')
fedor_fedorov.courses_attached += ['Python', 'Git']

lena_lenova = Lecturer('Lena', 'Lenova')
lena_lenova.courses_attached += ['Python', 'Git']

ivana_ivanova.assessment_for_lecturer(fedor_fedorov, 'Python', 9)
ivana_ivanova.assessment_for_lecturer(fedor_fedorov, 'Python', 8)
ivana_ivanova.assessment_for_lecturer(fedor_fedorov, 'Python', 7)
ivana_ivanova.assessment_for_lecturer(fedor_fedorov, 'Git', 9)
ivana_ivanova.assessment_for_lecturer(fedor_fedorov, 'Git', 8)
ivana_ivanova.assessment_for_lecturer(fedor_fedorov, 'Git', 10)
ivana_ivanova.assessment_for_lecturer(lena_lenova, 'Python', 8)
ivana_ivanova.assessment_for_lecturer(lena_lenova, 'Python', 7)
ivana_ivanova.assessment_for_lecturer(lena_lenova, 'Python', 9)
ivana_ivanova.assessment_for_lecturer(lena_lenova, 'Git', 9)
ivana_ivanova.assessment_for_lecturer(lena_lenova, 'Git', 10)
ivana_ivanova.assessment_for_lecturer(lena_lenova, 'Git', 8)

ivan_ivanov.assessment_for_lecturer(fedor_fedorov, 'Python', 9)
ivan_ivanov.assessment_for_lecturer(fedor_fedorov, 'Python', 8)
ivan_ivanov.assessment_for_lecturer(fedor_fedorov, 'Python', 7)
ivan_ivanov.assessment_for_lecturer(fedor_fedorov, 'Git', 8)
ivan_ivanov.assessment_for_lecturer(fedor_fedorov, 'Git', 7)
ivan_ivanov.assessment_for_lecturer(fedor_fedorov, 'Git', 7)
ivan_ivanov.assessment_for_lecturer(lena_lenova, 'Python', 8)
ivan_ivanov.assessment_for_lecturer(lena_lenova, 'Python', 10)
ivan_ivanov.assessment_for_lecturer(lena_lenova, 'Python', 7)
ivan_ivanov.assessment_for_lecturer(lena_lenova, 'Git', 9)
ivan_ivanov.assessment_for_lecturer(lena_lenova, 'Git', 7)
ivan_ivanov.assessment_for_lecturer(lena_lenova, 'Git', 10)

sidr_sidorov = Reviewer('Sidr', 'Sidorov')
sidr_sidorov.courses_attached += ['Python']
sidr_sidorov.courses_attached += ['Git']
sidr_sidorov.rate_hw(ivana_ivanova, 'Python', 8)
sidr_sidorov.rate_hw(ivana_ivanova, 'Python', 7)
sidr_sidorov.rate_hw(ivana_ivanova, 'Python', 10)
sidr_sidorov.rate_hw(ivan_ivanov, 'Python', 9)
sidr_sidorov.rate_hw(ivan_ivanov, 'Python', 8)
sidr_sidorov.rate_hw(ivan_ivanov, 'Python', 7)
sidr_sidorov.rate_hw(ivana_ivanova, 'Git', 10)
sidr_sidorov.rate_hw(ivana_ivanova, 'Git', 9)
sidr_sidorov.rate_hw(ivana_ivanova, 'Git', 10)
sidr_sidorov.rate_hw(ivan_ivanov, 'Git', 9)
sidr_sidorov.rate_hw(ivan_ivanov, 'Git', 10)
sidr_sidorov.rate_hw(ivan_ivanov, 'Git', 9)

katya_katusheva = Reviewer('Katya', 'Katusheva')
katya_katusheva.courses_attached += ['Python']
katya_katusheva.courses_attached += ['Git']
katya_katusheva.rate_hw(ivana_ivanova, 'Python', 5)
katya_katusheva.rate_hw(ivana_ivanova, 'Python', 8)
katya_katusheva.rate_hw(ivana_ivanova, 'Python', 10)
katya_katusheva.rate_hw(ivan_ivanov, 'Python', 10)
katya_katusheva.rate_hw(ivan_ivanov, 'Python', 8)
katya_katusheva.rate_hw(ivan_ivanov, 'Python', 7)
katya_katusheva.rate_hw(ivana_ivanova, 'Git', 8)
katya_katusheva.rate_hw(ivana_ivanova, 'Git', 7)
katya_katusheva.rate_hw(ivana_ivanova, 'Git', 10)
katya_katusheva.rate_hw(ivan_ivanov, 'Git', 4)
katya_katusheva.rate_hw(ivan_ivanov, 'Git', 10)
katya_katusheva.rate_hw(ivan_ivanov, 'Git', 8)

list_student = [ivana_ivanova, ivan_ivanov]
list_lectures = [fedor_fedorov, lena_lenova]

def list_of_commands():
    print('1 - список студентов и их данные;')
    print('2 - список лекторов и их данные;')
    print('3 - список проверяющих;')
    print('4 - оценки студентов по каждому курсу;')
    print('5 - оценки лекторов по каждому курсу;')
    print('6 - сравнение студентов по средней оценке за домашние задания')
    print('7 - сравнение лекторов по средней оценке')
    print('8 - средняя оценка за домашние задания по всем студентам в рамках курса')
    print('9 - Средняя оценка всех лекторов в рамках курса')
    return

def commands():
    while True:
        print('\n    Главное меню\n')
        command = input('Введите команду (* - список команд): ')
        if command == '*':
            list_of_commands()
        elif command == '1':
            print(f'Студент:\n{ivana_ivanova}')
            print(f'\nСтудент:\n{ivan_ivanov}')
        elif command == '2':
            print(f'\nЛектор:\n{fedor_fedorov}')
            print(f'\nЛектор:\n{lena_lenova}')
        elif command == '3':
            print(f'\nПроверяющий:\n{sidr_sidorov}')
            print(f'\nПроверяющий:\n{katya_katusheva}')
        elif command == '4':
            print(f'\nОценки ivana_ivanova по курсу Python:', ivana_ivanova.grades_student['Python'])
            print(f'Оценки ivana_ivanova по курсу Git:', ivana_ivanova.grades_student['Git'])
            print(f'\nОценки ivan_ivanov по курсу Python:', ivan_ivanov.grades_student['Python'])
            print(f'Оценки ivan_ivanov по курсу Git:', ivan_ivanov.grades_student['Git'])
        elif command == '5':
            print(f'\nОценки fedor_fedorov по курсу Python:', fedor_fedorov.grades_lecturer['Python'])
            print(f'Оценки fedor_fedorov по курсу Git:', fedor_fedorov.grades_lecturer['Git'])
            print(f'\nОценки lena_lenova по курсу Python:', lena_lenova.grades_lecturer['Python'])
            print(f'Оценки lena_lenova по курсу Git:', lena_lenova.grades_lecturer['Git'])
        elif command == '6':
            print(f'Сравнение студента ivana_ivanova > ivan_ivanov по средней оценке за домашние задания:', ivana_ivanova.student_average_grade() > ivan_ivanov.student_average_grade())
        elif command == '7':    
            print(f'Сравнение лектора fedor_fedorov < lena_lenova по средней оценке за домашние задания:', fedor_fedorov.lecturer_average_grade() < lena_lenova.lecturer_average_grade())
        elif command == '8':
            course = "Python"
            print(f'\nCредняя оценка за домашние задания по всем студентам в рамках курса {course}: {average_grade_on_course_student(course, *list_student)}')
            course = "Git"
            print(f'Cредняя оценка за домашние задания по всем студентам в рамках курса {course}: {average_grade_on_course_student(course, *list_student)}')
        elif command == '9':
            course = "Python"
            print(f'\nСредняя оценка всех лекторов в рамках курса {course}: {average_grade_on_course_lectures(course, *list_lectures)}')
            course = "Git"
            print(f'Средняя оценка всех лекторов в рамках курса {course}: {average_grade_on_course_lectures(course, *list_lectures)}')
        else:
            print('\033[31mВы ввели неверную команду\033[0m\n')
commands()

      