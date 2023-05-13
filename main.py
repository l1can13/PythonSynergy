from student import Student

name = 'Вася Пупкин'
age = 17
id = 1

student1 = Student(name, age, id)

print(student1.name)

student1.change_name('Витя Пупкин')

print(student1.name)
