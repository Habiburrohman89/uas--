from django.shortcuts import render

from .models import editor

def buku(request):
    tahu = editor.objects.all()
    context = {
        'wk': tahu,
    }
    return render(request,('nit.html'),context)
    
