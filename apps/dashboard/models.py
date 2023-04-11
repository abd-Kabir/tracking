from django.db import models

from config.models import BaseModel


class Track(BaseModel):
    order_num = models.CharField(max_length=20, null=True, blank=True)
    box = models.CharField(max_length=20, null=True, blank=True)
    container = models.TextField(null=True, blank=True)
    shipper = models.TextField(null=True, blank=True)
    cargo = models.TextField(null=True, blank=True)
    customer = models.TextField(null=True, blank=True)
    dispatch = models.DateField(null=True, blank=True)
    load_date = models.DateField(null=True, blank=True)
    agent = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    consignee = models.TextField(null=True, blank=True)
    price = models.BigIntegerField(null=True, blank=True)
    client_price = models.BigIntegerField(null=True, blank=True)
    extra_expense = models.BigIntegerField(null=True, blank=True)

    WAITING = 0
    GIVEN = 1
    STATUS_CHOICE = [
        (WAITING, 'Waiting'),
        (GIVEN, 'Given')
    ]
    status = models.SmallIntegerField(choices=STATUS_CHOICE, default=WAITING, null=True, blank=True)

    class Meta:
        db_table = 'Track'
