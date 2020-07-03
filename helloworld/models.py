from django.db import models


class People(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()
    email = models.CharField(max_length=128, null=True, blank=False)

    def __str__(self):
        return f'{self.name}'
