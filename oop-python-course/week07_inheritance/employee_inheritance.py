class Employee_TLD:
    def __init__(self_TLD, name_TLD, salary_TLD):
        self_TLD.name_TLD = name_TLD
        self_TLD.salary_TLD = salary_TLD

class Manager_TLD(Employee_TLD):
    def __init__(self_TLD, name_TLD, salary_TLD, department_TLD):
        super().__init__(name_TLD, salary_TLD)
        self_TLD.department_TLD = department_TLD

    def display_manager_TLD(self_TLD):
        print("Name:", self_TLD.name_TLD)
        print("Salary:", self_TLD.salary_TLD)
        print("Department:", self_TLD.department_TLD)

manager1_TLD = Manager_TLD("John", 50000, "IT")
manager1_TLD.display_manager_TLD()