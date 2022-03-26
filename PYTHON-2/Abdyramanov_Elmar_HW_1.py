class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self, fullname, age, is_married):
        print(f'fullname: {fullname} \n age: {age} \n is_married: {is_married} \n')

    def output(self):
        return f'fullname {self.fullname} \n age {self.age}\n is_married {self.is_married}\n'


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        Person.__init__(self, fullname, age, is_married)
        self.marks = marks

    def average_rating(self, ):
        print(sum(self.marks) / 5)


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience=3):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience
        self.salary = 16000

    def Teacher_wage(self):
        if self.experience > 3:
            new_salary = self.salary + (self.salary / 100 * 5) * (self.experience - 3)
            return new_salary


lecturer = Teacher('Askar', 30, 'married', 4)
print(f'{lecturer.fullname}, {lecturer.age} years old ,{lecturer.is_married}, '
      f'work experience {lecturer.experience} ')
print(lecturer.Teacher_wage())


def create_students():
    student_1 = Student(fullname="Roza", age=24, is_married='married', marks={
        "кыргыз-тили": 5,
        "алгебра": 4,
        "физиология": 5,
        "терапия": 2,
        "латынский-язык": 3,
    })
    student_2 = Student(fullname="Almazbek", age=17, is_married='idle', marks={
        "химия": 5,
        "русский-язык": 3,
        "математика": 4,
        "информатика": 5,
        "АЧД": 4,
    })
    student_3 = Student(fullname="Sadyr", age=27, is_married='married', marks={
        "астрономия": 3,
        "история": 3,
        "генетика": 2,
        "неврология": 3,
        "анатомия": 4,
    })

    results = student_1, student_2, student_3
    return results


students = create_students()
for i in students:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f'Name: {i.fullname}\n age: {i.age}\n is_married: {i.is_married}\n'
          f'Average marks: {sum(list) / len(list)}\n')
