class Inson:
    def __init__(self, ism="Ali", yosh=20):
        self.ism = ism
        self.yosh =yosh

    def show(self):
        print(self.ism, self.yosh)

class Talaba(Inson):
    def __init__(self, kurs=1, gpa=2.8):
        self.gpa = gpa
        self.kurs = kurs
        super().__init__()

    def show(self):
        print(self.kurs)
        super().__init__()

# c = Talaba(kurs=1, gpa=4)
# c.show()

class Bitiruvchi(Talaba):
    def __init__(self, diplom=True, yul = True):
        self.kurs = kurs
        self.yul = yul
        self.diplom = diplom
        super().__init__(kurs=4)

a = Bitiruvchi(diplom=False, yul=True)