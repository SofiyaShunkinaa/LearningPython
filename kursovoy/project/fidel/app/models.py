from django.db import models

class Master(models.Model):
    name = models.CharField(max_length=100)
    image_path = models.CharField(max_length=200) 
    services = models.TextField() 

    def __str__(self):
        return self.name
