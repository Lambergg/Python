import datetime

#Parent class Collective
class Collective:
    num_of_members = 0
    RAISE = 1.05

    def __init__(self,f_name, l_name, pay, job, rise):
        self.f_name = f_name
        self.l_name = l_name
        self.email = f_name + '.' + l_name + '@work.ru'
        self.payment = pay
        self.job = job
        self.rise = rise

        Collective.num_of_members += 1

    def fullname(self):
        return f'{self.f_name} {self.l_name}'

    def apply_raise(self):
        self.payment = self.payment * self.RAISE

    @classmethod
    def set_RAISE(cls, amount):
        cls.RAISE = amount

    @classmethod
    def from_string(cls, string):
        first_name, last_name, payment, job, rise = string.split('-')
        return cls(first_name, last_name, payment, job, rise)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 7:
            return False
        return True

#Child class Director

class Director(Collective):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        Director.__instance = None

    def __init__(self, f_name, l_name, pay, job, rise):
        super().__init__(f_name, l_name, pay, job, rise)
        self.job = job

class Assistant(Collective):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        Assistant.__instance = None

    def __init__(self, f_name, l_name, pay, job, rise):
        super().__init__(f_name, l_name, pay, job, rise)
        self.job = job

    def __repr__(self):
        return f"Assistant('{self.f_name}', '{self.l_name}')"


class Vector:

    def __init__(self, sol1, sol2):
        self.sol1 = sol1
        self.sol2 = sol2

    def __repr__(self):
        return f"Vector({self.sol1}, {self.sol2})"

    def __str__(self):
        return f"({self.sol1}, {self.sol2})"

    def __add__(self, other):
        return Vector(self.sol1 + other.sol1, self.sol2 + other.sol2)

v1 = Vector(2500,1700)
v2 = Vector(3000,5000)
print(v1)
print(v1 + v2)

print()
print(' Personnel ')
worker1 = Collective('Yuri', 'Pashenko', 90000, 'Serviceman', 0.5)
worker2 = Collective('Artem', 'Ivanov', 95000, 'Operator CNC', 0.3)
director = Director('Oleg', 'Otti', 300000, 'Director', 1.5)
assistant = Assistant('Igor', 'Kosheev', 200000, 'Assistant', 1.0)

print()
print(' In memory ')
print(worker1.fullname())
print(worker1)
print(worker2.fullname())
print(worker2)
print(director.fullname())
print(director)
print(assistant.fullname())
print(assistant)

print()
print(' Num of Members ')
print(Collective.num_of_members)

print()
print(' About ')
print(' Name - ', worker1.fullname())
print(' Job Title - ', worker1.job)
print(' Salary - ', worker1.payment)
print(' Email - ', worker1.email)
print(' Rise - ', worker1.rise)

print()
print(' About ')
print(' Name - ', worker2.fullname())
print(' Job Title - ', worker2.job)
print(' Salary - ', worker2.payment)
print(' Email - ', worker2.email)
print(' Rise - ', worker2.rise)

print()
print(' About ')
print(' Name - ', director.fullname())
print(' Job Title - ', director.job)
print(' Salary - ', director.payment)
print(' Email - ', director.email)
print(' Rise - ', director.rise)

print()
print(' About ')
print(' Name - ', assistant.fullname())
print(' Job Title - ', assistant.job)
print(' Salary - ', assistant.payment)
print(' Email - ', assistant.email)
print(' Rise - ', assistant.rise)

print()
print(' Salary increase percentage №1 ')
print(' General - ', Collective.RAISE)
print()
print(' Worker №1 - ', worker1.RAISE)
print(' Worker №2 - ', worker2.RAISE)
print(' Director - ', director.RAISE)
print(' Assistant - ', assistant.RAISE)
worker1.apply_raise()
worker2.apply_raise()
director.apply_raise()
assistant.apply_raise()

print()
print(' Increase Salary №1 ')
print(Collective.fullname(worker1))
print(worker1.payment)
print(Collective.fullname(worker2))
print(worker2.payment)
print(Collective.fullname(director))
print(director.payment)
print(Collective.fullname(assistant))
print(assistant.payment)

print()
print(' Salary increase percentage №2 ')
print(' General - ', Collective.RAISE)
print()
print(' Worker №1 - ', worker1.RAISE)
print(' Worker №2 - ', worker2.RAISE)
print(' Director - ', director.RAISE)
print(' Assistant - ', assistant.RAISE)
Collective.set_RAISE(1.9)
worker1.apply_raise()
worker2.apply_raise()
director.apply_raise()
assistant.apply_raise()

print()
print(' Increase Salary №2 ')
print(Collective.fullname(worker1))
print(worker1.payment)
print(Collective.fullname(worker2))
print(worker2.payment)
print(Collective.fullname(director))
print(director.payment)
print(Collective.fullname(assistant))
print(assistant.payment)

print()
print(' New Member ')
s1 = 'Vasya-Petrov-30000-Serviceman-0.6'
s2 = 'Petr-Lastochkin-20000-Operator CNC-0.75'
s3 = 'Stepan-Vasilev-350000-Director-2.0'
worker3 = Collective.from_string(s3)
print(' Name - ', worker3.fullname())
print(' Job Title - ', worker3.job)
print(' Salary - ', worker3.payment)
print(' Email - ', worker3.email)
print(' Rise - ', worker3.rise)

print()
date = datetime.date(2023,1,12)
print(Collective.is_workday(date))