from django.urls import path
from tshirt import views


urlpatterns = [
  path('', views.index, name='index'),
]
