from systems import world_file

familiar_witch_school = world_file.World("Litte Witch Academia Ripoff")
mbti_school = world_file.World("MBTI 2")

class School:
    def __init__(self, name):
        self.name = name

        self.students = []
        self.teachers = []
        self.classes = []

        self.schedule = Schedule()
        self.school_day = 0

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_class(self, class_):
        self.classes.append(class_)

class BoardingSchool(School):
    def __init__(self, name):
        self.name = name

        self.students = []
        self.teachers = []
        self.classes = []
        self.dorms = []

        self.schedule = Schedule()
        self.school_day = 0

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_class(self, class_):
        self.classes.append(class_)

    def add_dorm(self, dorm):
        self.dorms.append(dorm)


class Course:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []
        self.classrooms = []

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

    def add_student(self, student):
        self.students.append(student)


class Classroom:
    def __init__(self, name, location, teacher, class_size):
        self.name = name
        self.location = location
        self.teacher = teacher
        self.class_size = class_size
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class Dorm:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.rooms = []

    def add_student(self, student):
        self.students.append(student)

class DormRoom:
    def __init__(self, number):
        self.number = number
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class Schedule:
    def __init__(self):
        self.days = {}

    def add_day(self, day, schedule):
        self.days[day] = schedule

    def get_day(self, day):
        return self.days[day]

## Example Code
school3 = BoardingSchool("St. Luke's Academy")
schedule3 = Schedule()
school3.schedule = schedule3

schedule3.add_day("Day 1", {
    "08:00": "Breakfast",
    "09:00": "Potions",
    "10:00": "History",
    "11:00": "Magic",
    "12:00": "Lunch"
})