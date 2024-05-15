from django.db import models

class Master(models.Model):
    name = models.CharField(max_length=100)
    image_path = models.CharField(max_length=200) 
    services = models.TextField() 
    experience_years = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    def get_services_list(self):
        return self.services.split('\n')
    
    def get_experience_display(self):
        years = self.experience_years
        if 11 <= years % 100 <= 19:
            return f"{years} лет"
        elif years % 10 == 1:
            return f"{years} год"
        elif 2 <= years % 10 <= 4:
            return f"{years} года"
        else:
            return f"{years} лет"
        
    def get_name_with_ending(self):
        if self.name.endswith('а') or self.name.endswith('я'):
            return f"{self.name[:-1]}е"
        elif self.name.endswith('ий'):
            return f"{self.name[:-2]}ию"
        else:
            return f"{self.name}у"    
