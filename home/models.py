from django.db import models

class Restaurant(models.Model) :
    name = models.CharField(max_length = 255)
    address = models.TextField()
    contact = models.CharField(max_length = 20)
    operating_days = models.CharField(
        max_length = 100,
        help_text = "Comma-separated list of days(e.g., Mon,Tue,Wed,Thu,Fri,Sat,Sun)",
        blank = True,
        null = True
    )

    def __str__(self) :
        return self.name