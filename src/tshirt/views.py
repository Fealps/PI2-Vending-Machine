from django.shortcuts import render
from tshirt.models import Tshirt
from django.core.paginator import Paginator


def index(request, page=1):
  tshirts = Tshirt.objects.all()

  paginator = Paginator(tshirts, per_page=6)
  tshirt = paginator.get_page(page)
  context = {"tshirts": tshirt.object_list, "page_obj": tshirt}
  
  return render(request, 'index.jinja2', context)

def selectedTshirt(request, id):
  tshirt = Tshirt.objects.get(id=id)

  tshirts = list(Tshirt.objects.filter(name=tshirt.name).order_by('size'))
  
  context = {"tshirts": tshirts, "tshirt": tshirt}

  return render(request, 'selected-tshirt.jinja2', context)
