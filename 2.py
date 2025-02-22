import datetime
#-------------------------------------------------------------
class worker:
    
    num_of_workers = 0
    RAISE = 1.05
    
    def __init__(self, first_name, last_name, payment):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@hard.work'
        self.payment = payment
        
        worker.num_of_workers += 1

    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def apply_raise(self):
        self.payment = self.payment * self.RAISE
    
    @classmethod
    def set_RAISE(cls, amount):
        cls.RAISE = amount
        
    @classmethod
    def from_string(cls, string):
        first_name, last_name, payment = string.split('-')
        return cls(first_name, last_name, payment)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
class Assistant(worker):
    def __init__(self, first_name, last_name, payment, job):
        super().__init__(first_name, last_name, payment)
        self.job = job
#---------------------------------------------------------------------
print('')
print(' - КАДРОВАЯ СТАТСТИКА - ')
#---------------------------------------------------------------------
worker_1 = worker('Ivan', 'Ivanov', 10000)
worker_2 = worker('Petr', 'Petrov', 20000)
assistant_1 = Assistant('Stepan', 'Stepanov', 30000, 'main')
#---------------------------------------------------------------------
print('')
print(' - ЯЧЕЙКИ ПАМЯТИ:')  
print(worker_1.fullname())
print(worker_1)
print(worker_2.fullname())
print(worker_2)
print(assistant_1.fullname())
print(assistant_1)
#---------------------------------------------------------------------
print('')
print(' - КОЛИЧЕСТВО РАБОТНИКОВ:')  
print(worker.num_of_workers)
#---------------------------------------------------------------------
print('')
print(' - БАЗОВАЯ ИНФОРМАЦИЯ:')
print('')
print(worker_1.fullname())
print('ДОЛЖНОСТЬ -')
print('ЗАРПЛАТА -', worker_1.payment) 
print(worker_1.email)
print('')
print(worker_2.fullname())
print('ДОЛЖНОСТЬ -')
print('ЗАРПЛАТА -', worker_2.payment)   
print(worker_2.email)
print('')
print(assistant_1.fullname())
print('ДОЛЖНОСТЬ -', assistant_1.job)
print('ЗАРПЛАТА -', assistant_1.payment)   
print(assistant_1.email)
#---------------------------------------------------------------------
print('')
print(' - ПРОЦЕНТ ПОВЫШЕНИЯ ЗАРПЛАТЫ #1:') 
print('')
print('ОБЩИЙ - ', worker.RAISE)
print('РАБОТНИК №1 - ', worker_1.RAISE)
print('РАБОТНИК №2 - ', worker_2.RAISE)
worker_1.apply_raise()
worker_2.apply_raise()
print('')
print(' - ПОВЫШЕННАЯ ЗАРПЛАТА РАБОТНИКОВ #1:')
print('')
print(worker.fullname(worker_1)) 
print(worker_1.payment)
print(worker.fullname(worker_2))     
print(worker_2.payment)
#---------------------------------------------------------------------
print('')
worker.set_RAISE(1.07)
worker_1.apply_raise()
worker_2.apply_raise()
print(' - ПРОЦЕНТ ПОВЫШЕНИЯ ЗАРПЛАТЫ #2:') 
print('')
print('ОБЩИЙ - ', worker.RAISE)
print('РАБОТНИК №1 - ', worker_1.RAISE)
print('РАБОТНИК №2 - ', worker_2.RAISE)
print('')
print(' - ПОВЫШЕННАЯ ЗАРПЛАТА РАБОТНИКОВ #2:')
print('')
print(f'{worker_1.first_name} {worker_1.last_name}') 
print(worker_1.payment)  
print(f'{worker_2.first_name} {worker_2.last_name}')   
print(worker_2.payment)
#-------------------------------------------------------------
print('')
str_1 = 'Ivan-Ivanov-1000'
str_2 = 'Petr-Petrov-2000'
str_3 = 'Stepan-Stepanov-3000'
worker_3 = worker.from_string(str_3)
#-------------------------------------------------------------
print('')
my_date = datetime.date(2023,10,28)
print(worker.is_workday(my_date))
#-------------------------------------------------------------
# print('')
# help(Assistant)
# print(worker_1.__dict__)
# print(worker.__dict__)
 



