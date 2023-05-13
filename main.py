from student import Student

name = 'Вася Пупкин'
age = 16
id = 1


student1 = Student(name, age, id)

print(student1.name)

student1.change_name('Витя Пупкин')

print(student1.name)

student1.get_birth_year()

print(student1.get_birth_year())