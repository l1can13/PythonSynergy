from student import Student

name = 'Вася Пупкин'
age = 17
id = 1
fakultet = 'медицинский'

student1 = Student(name, age, id)

print(student1.fakultet)

student1.change_fakultet('медицинский')

print(student1.fakultet)
