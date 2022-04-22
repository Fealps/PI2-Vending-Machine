from django.urls import path
from tshirt import views


urlpatterns = [
  path('tshirt/<int:page>', views.index, name='tshirts'),
  path('', views.index, name='tshirt'),
  path('tshirt/selection/', views.selectedTshirt, name='selectedTshirt')
]
