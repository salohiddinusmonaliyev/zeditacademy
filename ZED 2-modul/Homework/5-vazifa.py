"""
7/23/2022
Usmonaliyev Salohiddin

"""

# # 1-vazifa
# with open("files/ismlar.txt") as f:
#     a = f.readlines()
# for i in range(0, 5):
#     print(f"line {i}:", a[i])

# # 2-vazifa
# while True:
#     a = input("Ism kiriting:")
#     b = input("Yana ism kiritasizmi (yes/not): ")
#     with open("files/ismlar.txt", 'a') as f:
#         f.write(a+"\n")
#     if b=='not':
#         break

# # 3-vazifa
# with open("files/ismlar.txt", 'r') as f:
#     a = f.readlines()
#     for i in a:
#         print(i)

# # 4-vazifa
# for i in range(5):
#     a = input("Ism kiriting:")
#     with open("files/ismlar.txt", 'a') as f:
#         f.write(a+"\n")

# # 5-vazifa
# a = input("Qaysi kitbni olasiz: ").lower()
# with open('kitoblar.txt', 'r') as fayl:
#     b = fayl.read()
#     if a in b:
#         print("Siz kitobni olishingiz mumkin")
#     else:
#         print("Siz so’ragan kitob hozircha yo’q")
#         with open('kitoblar.txt', 'a') as fayl:
#             fayl.write(a+"\n")

# # 6-vazifa
# with open("files/pi_million_digits.txt", 'r') as file:
#     a = file.read()
#     if '050908' in a:
#         print("Bor")
#     else:
#         print("yo'q")