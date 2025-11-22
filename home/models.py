from django.db import models
import datetime

class DailySpecialManager(models.Manager) :
    def upcoming(self) :
        today = datetime.date.today()
        return super().get_queryset().filter(special_date_gte = today)
class DailySpecial(models.Model) :
    name = models.CharField(max_length = 255)
    description = models.TextField()
    special_date = models.DateField()

    objects = DailySpecialManager

    def __str__(self) :
        return f"{self.name} - {self.special_date}"