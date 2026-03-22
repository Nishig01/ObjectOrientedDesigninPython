#Class methods = Allow operations related to the class itself
                 # Take (cls) as the first parameter, which represents the class itself.
# Instance methods take (self) as the first parameter

# Instance methods -for operations on instances if the lass(objectS)
# Static methods - for utility functions that do not need access to class data
# Class methods - best for class-level data or require access to the class itself

class Student:
    count =0
    total_gpa=0
    def __init__(self, name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 #whenever student object is created increment student count by 1
        Student.total_gpa+=gpa

    # this is an instance method
    def get_info(self): #referring to the object we are currently working with
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total no. of studnets {Student.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count ==0:
            return 0
        else :
            return f"Average gpa: {Student.total_gpa/cls.count:.2f}"

studnet1 = Student("Nishi", 4.0)
studnet2 = Student("Manya", 3.6)
studetn3 = Student("dahu", 4.0)
print(Student.get_count())
print(Student.total_gpa)
print(Student.get_avg_gpa())
