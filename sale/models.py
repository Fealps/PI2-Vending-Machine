from django.db import models
from django.utils import timezone
from django.conf import settings
from tshirt.models import Tshirt


class Sale(models.Model):
    createdAt = models.DateTimeField(default=timezone.now)
    #paymentMethod = models.ForeignKey()
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
    status = models.IntegerField()
