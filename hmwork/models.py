from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

# Create your models here.

class Hospital(models.Model):
    h_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    hopital_img = models.ImageField(upload_to='media/')
    owner_name = models.CharField(max_length=200)
    email = models.EmailField()
    city = models.CharField(max_length=200)
    addresh = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Doctor(models.Model):
    d_id = models.AutoField(primary_key=True)
    hospital_id = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    degree = models.CharField(max_length=200)
    contact = models.IntegerField()
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    data_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Stap(models.Model):
    s_id = models.AutoField(primary_key=True)
    hospital_id = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    email = models.EmailField()
    degree = models.CharField(max_length=200)
    contact = models.IntegerField()
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    data_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name


class Pasent(models.Model):
    p_id = models.AutoField(primary_key=200)
    hospital_id = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField(default='optional')
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    age = models.IntegerField()
    GENDER = (('MALE','MALE'),('FEMALE','FEMALE'),('OTHER','OTHER'))
    gander = models.CharField(max_length=200,choices=GENDER)
    date_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name









