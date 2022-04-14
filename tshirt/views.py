from django.shortcuts import render
from tshirt.models import Tshirt


def index(request):
  tshirts = Tshirt.objects.all()
  context = {
    "tshirts": tshirts
  }
  
  return render(request, 'index.jinja2', context)
