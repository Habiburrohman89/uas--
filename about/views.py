from django.shortcuts import render

from .models import mhs
from .models import skripsi
from .models import th


def tahu(request):
    habib = mhs.objects.all()
    context = {
        'nita': habib,
    }
    return render(request,'about.html',context)
def bh(request):
    nt = skripsi.objects.all()
    context = {
        'nb': nt,
    }
    return render(request,'bg.html',context)

def hp(request):
    nb = th.objects.all()
    context = {
        'kb': nb,
    }
    return render(request,'pck.html',context)
