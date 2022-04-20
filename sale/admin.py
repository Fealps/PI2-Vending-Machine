from django.contrib import admin
from sale.models import Sale, PaymentFactory

admin.site.register(PaymentFactory)
admin.site.register(Sale)
