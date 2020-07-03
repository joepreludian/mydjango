from django.db import models


class People(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'
