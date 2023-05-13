class Student:
    def __init__(self, name, age, id,):
        self.name = name
        self.age = age
        self.id = id
        self.salary = None

    def change_name(self, new_name):
        self.name = new_name
        
    def set_salary(self, salary):
        self.salary = salary
        
    def get_num_letters_name(self):
        num_lett = len(self.name)
        return num_lett
