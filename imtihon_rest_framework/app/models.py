from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Suv(models.Model):
    brend = models.CharField(max_length=50)
    narx = models.IntegerField()
    litr = models.CharField(max_length=50)
    batafsil = models.TextField()

    def __str__(self):
        return self.brend

class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    qarz = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Admin(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.IntegerField()
    ish_vaqti = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Haydovchi(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    kiritilgan_sana = models.DateField()

    def __str__(self):
        return self.ism

class Buyurtma(models.Model):
    date = models.DateField()
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdori = models.CharField(max_length=50)
    narx = models.IntegerField()
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)

    def __str__(self):
        return self.suv
