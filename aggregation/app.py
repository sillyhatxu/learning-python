from marshmallow import Schema, fields, pprint

#  aggregation 聚合

class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


class StudentSchema(Schema):
    name = fields.Str()
    major = fields.Str()
    gpa = fields.Float()
    is_on_probation = fields.Boolean()


class Teacher:

    def __init__(self, name, studentList=None):
        self.studentList = studentList
        self.name = name


class TeacherSchema(Schema):
    name = fields.Str()
    studentList = fields.List(fields.Nested(StudentSchema, ref='StudentSchema'))


studentList = list()
student1 = Student("Jim", "Business", 3.8, False)
student2 = Student("Pam", "Art", 2.5, True)
studentList.append(student1)
studentList.append(student2)

teacher = Teacher("Cookie", studentList)

schema = TeacherSchema()
result = schema.dump(teacher)
pprint(result.data)

# print(teacher.name)
# print(teacher.studentList)
# print(teacher.studentList[0])
