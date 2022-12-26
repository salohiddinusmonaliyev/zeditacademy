"""
class User:
    def __init__(self, i, y, m):# konsruktor
        self.ism = i
        self.yosh = y
        self.manzil = m
        print(f"{i} ismli foydalanuchi yaraldi")

user1 = User("Ali", 20, "Toshkent")
user2 = User("Sam", 18, "New York")
user3 = User("Vali", 22, "Farg'ona")
"""

class Animal:
    def __init__(self, n, y, t, m, os):
        self.yegulik = y
        self.tur = t
        self.manzil = m
        self.nomi = n
        self.oyoq = os

    def show(self):
        if self.tur:
            self.tur = "yirtqich"
        else:
            self.tur = "o'txo'r"
        print(f"{self.nomi}:\nYashash joyi: {self.manzil}\nYuguligi: {self.yegulik}\nTuri: {self.tur}\nOyoqlar soni: {self.oyoq}")

anilmal1 = Animal("yo'lbars", "go'sht", "yirtqich", "Afrika", "4 ta")

anilmal1.show()