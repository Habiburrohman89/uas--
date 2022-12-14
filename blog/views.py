from django.shortcuts import render

from .models import blog
from .models import aldi


def index(request):
    
    yuk = blog.objects.all()
    context = {
        'title': 'habib',
        'ygy': yuk,
    }
    return render(request,'blog.html',context)

def tahu(request):

    habib = aldi.objects.all()
    context = {
        'iklil': habib,
    }
    return render(request,'tahu.html',context)