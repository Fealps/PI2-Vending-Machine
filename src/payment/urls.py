from django.urls import path
from payment import views

app_name = "payments"
urlpatterns = [
    path('payment/<int:id>', views.payment, name='payment'),
]
