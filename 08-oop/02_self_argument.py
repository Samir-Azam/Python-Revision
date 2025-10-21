# self argument in python is passed in each and every methods of class so that the reference of object is maintained

class Students:
    name = "student"
    department = "Computer"

    def print_info(self):
        print(f"Name is {self.name} and department is {self.department}")
    
    def update_info(self, name, department):
        self.name = name
        self.department = department
        print(f"Updated info {self.name} is in {self.department} department")

# object creation

student1 = Students()

student1.print_info()
student1.update_info("Rahul", "Civil")

Students.update_info(student1, "Rohit", "Chemical")