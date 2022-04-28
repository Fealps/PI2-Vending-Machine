from django.shortcuts import render
from payment.models import Payment
from tshirt.models import Tshirt
from pixqrcode import PixQrCode


def payment(request, id):
  tshirt = Tshirt.objects.get(id=id)
  payment = Payment.objects.create()
  name = ""
  mobile = ""
  city = "Brasília"
  amount = str(tshirt.price)
  pix = PixQrCode(name, mobile, city, amount)
  pix.save_qrcode("/vendingmachine/src/payment/static/img",
                  f"pix-{payment.id}")

  context = {"path": f"/img/pix-{payment.id}.png"}
  return render(request, 'pix-payment.jinja2', context)
