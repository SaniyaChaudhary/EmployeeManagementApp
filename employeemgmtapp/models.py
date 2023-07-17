from django.db import models

# Create your models here.

class Employee (models.Model):
    name = models.CharField(max_length=200)
    empId = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    working= models.BooleanField(default=True)
    department = models.CharField(max_length=15)

    #overring __str__ method
    def __str__(self):
     return self.name
    

class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    picture=models.ImageField(upload_to="testimonials/")
    rating=models.IntegerField(max_length=1)

    #overring __str__ method
    def __str__(self):
     return self.name


