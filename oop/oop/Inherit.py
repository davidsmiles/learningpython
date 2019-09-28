class Student:

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    hello = 15

    def __init__(self, name,  school, salary):
        super(WorkingStudent, self).__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 37.5


dave = WorkingStudent('David', 'UNIBEN', 30)
print(dave.school)

class Foo:

    @classmethod
    def hi(cls):
        print("Hello David")


foo = Foo()
foo.hi()


class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take parameters')


bar = Bar()
bar.hi()
