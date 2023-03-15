from django.shortcuts import render, get_object_or_404
from .models import Store, Tub
from django.db.models import Sum

# Create your views here.


def tubs_view(request):
    tubs = Tub.objects.all()
    return render(request, 'distribution/tubs.html', {'tubs': tubs})


def stores_view(request):
    stores = Store.objects.all()
    return render(request, 'distribution/stores.html', {'stores': stores})


def store_view(request, id):
    store = get_object_or_404(Store, id=id)
    tubs = Tub.objects.filter(store=store)
    total_volume = tubs.aggregate(Sum('size'))['size__sum']
    return render(request, 'distribution/store.html',
                  {'store': store, 
                   'tubs': tubs, 
                   'total_volume': total_volume})
