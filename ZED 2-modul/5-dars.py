"""
7/23/2022
Fayllar bilan ishlash | Pickle
"""
f = open("Homework/files/ismlar.txt")
while True:
    ask = input("salom: ")

    if ask=="s":
        a = f.readline()
        print(a)


