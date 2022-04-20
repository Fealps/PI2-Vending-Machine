from django.db import models
from django.utils import timezone
from tshirt.models import Tshirt


class PaymentFactory(models.Model):
   name = models.CharField(max_length=30, blank=False)



class Sale(models.Model):
    createdAt = models.DateTimeField(default=timezone.now)
    paymentMethod = models.ForeignKey(PaymentFactory, on_delete=models.CASCADE)
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
    status = models.IntegerField()
