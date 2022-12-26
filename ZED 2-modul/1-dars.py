# class Cars:
#     narhi = 300000000
#     rangi = "qora"
#     nomi = "malibu"
#     yil = "2021-yil"
#     brend = "Chevrolet"
#     number = "40 | G012TA"
#     def start(self):
#         print(f"{self.nomi} yurdi, Avtomobil raqami: {self.number}")
#     def stop(self):
#         print(f"{self.nomi} to'xtadi, Avtomobil raqami: {self.number}\n")
#     def tezlanish(self):
#         print(f"{self.nomi} tezlashdi, Avtomobil raqami: {self.number}")
#     def sekinlanish(self):
#         print(f"{self.nomi} sekinlashdi, Avtomobil raqami: {self.number}")
# c1 = Cars()
# c1.nomi = "nexia"
# c1.narhi = "100000000"
# c1.number = "40 | Q141RA"
#
# c = Cars()
# c.start()
# c.tezlanish()
# c.sekinlanish()
# c.stop()
#
# c1.start()
# c1.tezlanish()
# c1.sekinlanish()
# c1.stop()




import requests


r = requests.request(method="GET", url="https://islomapi.uz/api/present/day?region=Toshkent")
print(r.json())