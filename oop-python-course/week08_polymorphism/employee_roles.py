class Employee_TLD:
    def work_TLD(self_TLD):
        print("Employee performs tasks")

class Programmer_TLD(Employee_TLD):
    def work_TLD(self_TLD):
        print("Programmer writes code")

class Designer_TLD(Employee_TLD):
    def work_TLD(self_TLD):
        print("Designer creates UI designs")

employees_TLD = [Programmer_TLD(), Designer_TLD()]
for emp_TLD in employees_TLD:
    emp_TLD.work_TLD()