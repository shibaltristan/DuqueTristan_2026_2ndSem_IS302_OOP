class Employee_TLD:
    def __init__(self_TLD, name_TLD):
        self_TLD.__name_TLD = name_TLD
        self_TLD.__salary_TLD = 0

    def set_salary_TLD(self_TLD, salary_TLD):
        if salary_TLD > 0:
            self_TLD.__salary_TLD = salary_TLD

    def get_salary_TLD(self_TLD):
        return self_TLD.__salary_TLD

emp_TLD = Employee_TLD("Ana")
emp_TLD.set_salary_TLD(30000)
print("Salary:", emp_TLD.get_salary_TLD())