from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    ad_num=models.IntegerField()
    department=models.CharField(max_length=100)
    
class Profile(models.Model):
    student=models.OneToOneField(Student, on_delete=models.CASCADE)
    description=models.CharField(max_length=100)

class Book(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    pub_date=models.DateField()
    
class Books(models.Model):
    title=models.CharField(max_length=50)
    pub_date=models.DateField()
    author=models.CharField(max_length=50,default=0)
    image=models.ImageField(upload_to='gallery/',default=0)
    fl=models.FileField(upload_to='document/',default=0)

    
    
    
    
#CRUD -create,read,update,delete
#obj=Student(name=abc,age=sd,ad_num=cdg)
#obj.save()
#Student.object.all()