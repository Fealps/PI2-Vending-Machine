from django.db import models
from django.contrib.postgres.fields import ArrayField


class Size(models.Model):
  name = models.CharField(max_length=30)
  measure = ArrayField(
      models.FloatField(default=0),
      size=3,)

class Tshirt(models.Model):
  name = models.CharField(max_length=30, blank=False)
  description = models.TextField(
      max_length=100, blank=True)  # not sure is needed
  color = models.CharField(max_length=30, blank=False)
  price = models.FloatField(blank=False, default=0.00)
  qtyInStock = models.IntegerField(default=1)
  photo = models.ImageField(upload_to='tshirt/static/img/tshirts/', null=True)
  size = models.ForeignKey(Size, null=True, on_delete=models.CASCADE)

  class Gender(models.IntegerChoices):
    MALE = 0
    FEMALE = 1
    UNISEX = 2
  
  gender = models.IntegerField(choices=Gender.choices, blank=False)

  @property
  def photo_url(self):
    if self.photo and hasattr(self.photo, 'url'):
        return self.photo.url
