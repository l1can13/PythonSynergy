class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.birthday = None

    def change_name(self, new_name):
        self.name = new_name

    def get_birth_year(self):
        Sdata = 2023
        birthday = Sdata - self.age
        return birthday
