from django.db import models

# Create your models here.


class Meal(models.Model):
    image = models.ImageField(upload_to='meals')
    name = models.CharField(max_length=255)
    desc = models.TextField()
    
    is_diabetic = models.BooleanField(default=False)
    region = models.CharField(max_length=12, choices=[
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
        ])
    gain_weight = models.BooleanField(default=False)
    time = models.CharField(max_length=12, choices=[
        ('breakfast', 'BreakFast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ])
    
    def __str__(self) -> str:
        return f"{self.name}"
    
