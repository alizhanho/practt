class Employee:
    company_name = "TechCorp"  # class variable

    def __init__(self, name):
        self.name = name  #instance variable


emp1 = Employee("John")
emp2 = Employee("Sara")

print(emp1.company_name)
print(emp2.company_name)

# Change class variable
Employee.company_name = "NewTech"

print(emp1.company_name)
print(emp2.company_name)