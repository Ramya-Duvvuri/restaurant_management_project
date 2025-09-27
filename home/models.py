from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return {self.name} - {self.email}
class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
class MenuCategory(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name