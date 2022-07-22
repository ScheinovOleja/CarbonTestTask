from django.db import models


# Create your models here.


class CourierDetail(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя курьера')
    surname = models.CharField(max_length=32, verbose_name='Фамилия курьера')
    phone = models.CharField(max_length=16, verbose_name='Номер телефона')
    count_delivery = models.IntegerField(verbose_name='Общее количество доставок', null=True)
    area = models.ManyToManyField('delivery.DeliveryArea',
                                  verbose_name='Зоны, внутри которых курьер осуществляет доставку')
