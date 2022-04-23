from pickle import TRUE
from django.db import models
from django.utils import timezone
from tshirt.models import Tshirt
from payment.models import Payment



class Sale(models.Model):
    createdAt = models.DateTimeField(default=timezone.now)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
    status = models.IntegerField()
