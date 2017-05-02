class ContainStudents:

    all_students = []

    class __metaclass__(type):
        def __iter__(self):
            for stdnt in ContainStudents.all_students:
                yield stdnt

    class Student(object):

        def __init__(self,name,id):
            self.name = name
            self.id = id

        def get_student(self):
            nm = self.name
            id = self.id
            return (nm, id)

        def __repr__(self):
            return "Student({0}, {1})".format(self.name, self.id)

    def add_student(self,name,id):
        stdnt = ContainStudents.Student(name,id)
        ContainStudents.all_students.append(stdnt)
        print("Successfully added {0} to container".format(str(stdnt)))

contained = ContainStudents()
print contained.all_students

contained.add_student("Tim",20552660)
contained.add_student("Christine", 20552678)

print contained.all_students

list(ContainStudents)
