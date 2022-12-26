"""
USMONALIYEV SALOHIDDIN
2-vazifa
Backend Python3-2022
"""
"""
# 1-topshiriq
class Mehmon:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        print("Yangi mehmon bor")

    def about(self):
        print(f"Assalomu aleykum, men {self.name}. Yoshim {self.age} da. Elektron pochtam {self.email}.")

mehmon1 = Mehmon(name="Ali", age=18, email="ali@example.com")
mehmon1.about()
mehmon2 = Mehmon(name="Vali", age=20, email="valijon@example.com")
mehmon2.about()
"""
"""
# 2-topshiriq
class Student:
    def __init__(self, name, mgrade, egrade, hgrade):
        self.name = name
        self.math = mgrade
        self.en = egrade
        self.his = hgrade
    def average_grade(self):
        print(f"{self.name}\n3 ta fandan o'ratcha bahosi: {(self.en+self.his+self.math)/3}")

student1 = Student("Ali", 5, 4, 5)
student2 = Student("Vali", 4, 5, 4)
student1.average_grade()
student2.average_grade()
"""