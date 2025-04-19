from django.db import models
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    def __str__(self):
        return self.tarea
    

# Create your models here.

