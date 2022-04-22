from django.shortcuts import render
from tshirt.models import Tshirt
from django.core.paginator import Paginator


def index(request, page=1):
  tshirts = Tshirt.objects.all()

  paginator = Paginator(tshirts, per_page=6)
  tshirt = paginator.get_page(page)
  context = {"tshirts": tshirt.object_list, "page_obj": tshirt}
  
  return render(request, 'index.jinja2', context)

def selectedTshirt(request):

  return render(request, 'selected-tshirt.jinja2')
