class Employeetld:
    def work(self):
        print("Employee performs tasks")

class Programmartld(Employeetld):
    def work(self):
        print("Programmer writes code")

class Designertld(Employeetld):
    def work(self):
        print("Designer creates UI designs")

employeestld = [Programmartld(), Designertld()]
for emptld in employeestld:
    emptld.work()