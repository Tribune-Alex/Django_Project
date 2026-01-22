from django.db import models

class Lectures(models.Model):
    First_Name = models.CharField(max_length=45)
    Last_Name  = models.CharField(max_length=50)
    Subject = models.CharField(max_length=25)

class Courses(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=1)
    lecturer = models.ForeignKey(Lectures,on_delete=models.CASCADE)

class Students(models.Model):
    First_Name = models.CharField(max_length=35)
    Last_Name  = models.CharField(max_length=40)
    Age  = models.IntegerField()
    Nationality = models.TextField(null=True, blank=True)
    courses = models.ManyToManyField(Courses)



