from django.shortcuts import render, redirect
from djangoshoeapp.forms import ShoesAppForm
from djangoshoeapp.models import Shoes


# Create your templates here.
def shoes(request):
    if request.method == 'POST':
        form = ShoesAppForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
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


def destroy(request, id):
    shoes = Shoes.objects.get(id=id)
    shoes.delete()
    return redirect('/show')
