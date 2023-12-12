from django.db import models

# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    #text=models.TextField(null=True)
    def __str__(self):
        return self.caption
    
class Text(models.Model):
    name=models.CharField(max_length=50)
    text=models.TextField(null=True)
    def __str__(self):
        return self.name
