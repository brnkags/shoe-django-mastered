from django.shortcuts import render, redirect
from djangoshoeapp.forms import ShoesAppForm
from djangoshoeapp.models import Shoes
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient


# Create your templates here.
def shoes(request):
    form = ShoesAppForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        form = ShoesAppForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    shoes = Shoes.objects.all()
    return render(request, 'show.html', {'shoes': shoes})


def edit(request, id):
    shoes = Shoes.objects.get(id=id)
    return render(request, 'edit.html', {'shoes': shoes})


def update(request, id):
    shoes = Shoes.objects.get(id=id)
    form = ShoesAppForm(request.POST, instance=shoes)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'shoes': shoes})


def check_out(request, id):
    shoes = Shoes.objects.get(id=id)
    return render(request, 'checkout.html', {'shoes': shoes})


def mpesa(request, id):
    shoes = Shoes.objects.get(id=id)
    if request.method == 'POST':
        amount = shoes.shoeprice
        p_number = request.POST.get('phone_number')
        if not p_number or not p_number.isdigit:
            return HttpResponse('invalid phone number')
        if not amount or not amount.isdigit:
            return HttpResponse('invalid price')
        cl = MpesaClient()
        phone_number = p_number
        amount = int(amount)
        account_reference = 'BRIAN KICKS EMPIRE'
        transaction_desc = 'paying for sweet kicks'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)
    else:
        return render(request, "checkout.html", {"shoes": shoes})


def destroy(request, id):
    shoes = Shoes.objects.get(id=id)
    shoes.delete()
    return redirect('/show')
