from django.db import models
class register_tb(models.Model):
    Name = models.CharField(max_length = 20)
    Age = models.CharField(max_length = 20)
    phone_no = models.CharField(max_length = 20)
    Address = models.CharField(max_length = 20)
    Gender = models.CharField(max_length = 20)
    Username = models.CharField(max_length = 20,default="none")
    password = models.CharField(max_length = 20)
    
class image_tb(models.Model):
    image=models.FileField()
    
class city_tb(models.Model):
    city = models.CharField(max_length =30)
class place_tb(models.Model):
    name=models.CharField(max_length=20)
    cid=models.ForeignKey(city_tb,on_delete=models.CASCADE)
