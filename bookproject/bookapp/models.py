from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=250)
    auth=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')
    year=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
