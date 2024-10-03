class Student:

    def __init__(self, Fname, Lname, Course, Group, Year):
        self.NewName = Fname
        self.NewLname = Lname
        self.NewCourse = Course
        self.NewGroup = Group
        self.NewYear = Year

    def NewStudent(self):
        return f'Имя:{self.NewName} Фамилия:{self.NewLname} Курс:{self.NewCourse} Группа:{self.NewGroup} Год:{self.NewYear}'


n = input('Введите ваше имя:')
ln = input('Введите вашу фамилию::')
c = int(input('Введите ваш курс:'))
g = int(input('Введите вашу группу:'))
y = int(input('Введите ваш год рождения:'))

student1 = Student(n, ln, c, g, y)
print(student1.NewStudent())