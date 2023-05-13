from random import randint

class Student:
    def __init__(self, name, age, id,):
        self.name = name
        self.age = age
        self.id = id
        self.birthday = None
        self.salary = None

    def change_name(self, new_name):
        self.name = new_name

    def get_birth_year(self):
        Sdata = 2023
        birthday = Sdata - self.age
        return birthday

    def change_name(self, new_name):
        self.name = new_name
    
    def get_avg_mark(self):
        return randint(0, 5)
        
    def set_salary(self, salary):
        self.salary = salary
        
    def get_num_letters_name(self):
        num_lett = len(self.name)
        return num_lett
