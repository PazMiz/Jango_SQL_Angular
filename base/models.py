from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name



class Books(models.Model):
    bookname = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    date = models.IntegerField()
    list_display = ['bookname', 'writer', 'date']

    def __str__(self):
        return self.bookname



class School(models.Model):
    Teacher= models.CharField(max_length=255)
    studenets = models.CharField(max_length=255)
    grade = models.IntegerField()

    def __str__(self):
        return self.Teacher
    

    