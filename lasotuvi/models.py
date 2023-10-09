from django.db import models

# Create your models here.
# Trong file models.py của ứng dụng
from django.db import models

class Laso(models.Model):
    image_data = models.TextField()
    hoten = models.CharField(max_length=255)
    ngaysinh = models.CharField(max_length=255)
    thangsinh = models.CharField(max_length=255)
    namsinh = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.image_data,self.hoten,self.ngaysinh,self.thangsinh,self.namsinh}'