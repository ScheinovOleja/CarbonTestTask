from django.db import models

# Create your models here.


class DeliveryArea(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название зоны')
    of = models.JSONField(verbose_name='Координаты зоны доставки')
    to = models.JSONField(verbose_name='Координаты зоны доставки')

    def __str__(self):
        return f'{self.name}'
