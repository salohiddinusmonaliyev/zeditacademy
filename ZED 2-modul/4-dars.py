while True:
    a = input("Ism kiriting: ").title()
    if a=="Stop":
        break
    with open("Homework/files/ismlar.txt", 'a') as file:
        file.write(a + "\n")

with open("Homework/files/ismlar.txt") as f:
    b = f.read()
print("Siz kiritgan ismlar: ", b.replace("\n", ", "))