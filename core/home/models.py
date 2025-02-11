from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    # image = models.ImageField()
    file = models.FileField()

class Car(models.Model):
    def __str__(self):
        return self.car_name + ' -> ' + str(self.speed)

    car_name = models.CharField(max_length=255)
    speed = models.IntegerField(default=20)
