# coding=UTF-8

class SchoolMember:
    """代表任何学校里的成员。"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我有关的细节'''
        # end 参数用在超类的 tell() 方法的 print 函数中，目的是打印一行并允许下一次打印在同一行继续。
        # 这是一个让 print 能够不在打印的末尾打印出 \n （ 新行换行符） 符号的小窍门。
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end =" ")

class Teacher(SchoolMember):
    '''代表一位老师。'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    #'''代表一位学生'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# 打印一行空白行
print()

members = [t, s]
for member in members:
    member.tell()