from django.db import models
<<<<<<< HEAD
class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
=======

class MenuCategory(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
>>>>>>> b9505b816562e7dbfd339e0060228d84e8cfb298
