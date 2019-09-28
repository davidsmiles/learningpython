class Student:

    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student('David James', [70, 50, 23, 56])
print(Student.average(student_one))


class Garage:

    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

    def __repr__(self):
        return f'<Garage {self.cars}'

    def __str__(self):
        return f'Garage with {len(self.cars)} cars'


ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

for car in ford:
    print(car)

print(ford)