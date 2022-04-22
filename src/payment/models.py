from django.db import models

class Payment(models.Model):
  name = models.CharField(max_length=30, default="PIX", blank=True)

