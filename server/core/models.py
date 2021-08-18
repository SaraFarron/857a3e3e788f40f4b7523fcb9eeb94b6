from django.db import models


class Function(models.Model):
    function = models.CharField(max_length=128)
    dt = models.FloatField()
    interval = models.FloatField()

    def __str__(self):
        return self.function
