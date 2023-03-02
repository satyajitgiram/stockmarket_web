from django.db import models

# Create your models here.
# class 

class Requestcallback(models.Model):
    phone_number = models.CharField(max_length=15,null = True, blank = True, default='+910000000000')
    full_name = models.CharField(max_length=255) 
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self) -> str:
        return self.full_name 