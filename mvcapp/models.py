from django.db import models

# Create your models here.
class Student(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Email = models.EmailField(unique=True)
    Dept = models.CharField(max_length=20)

    class Meta:
        db_table = 'Student_Master'

