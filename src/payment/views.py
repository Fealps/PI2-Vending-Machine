import os.path
from django.shortcuts import render
from payment.models import Payment
from tshirt.models import Tshirt
from pixqrcode import PixQrCode


def payment(request, id):
  tshirt = Tshirt.objects.get(id=id)
  payment = Payment.objects.create()
  name = "Martha Dantas Silva"
  mobile = "61991302532"
  city = "Brasília"
  amount = str(tshirt.price)
  pix = PixQrCode(name, mobile, city, amount)
  if os.path.isfile(f"/ img/pix.png"):
    path = f"/img/pix.png"
  else:
    pix.save_qrcode("/vendingmachine/src/payment/static/img",
                  f"pix")
    path = f"/img/pix.png"

  context = {"path": path, "tshirt": tshirt}
  return render(request, 'pix-payment.jinja2', context)
