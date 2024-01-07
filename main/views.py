from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def main(request):
    service=Our_Service.objects.all()
    client=Client.objects.all()
    contact=Contact.objects.all()
    ourguard=OurGuard.objects.all()


    context={
        'service':service,
        'client':client,
        'contact':contact,
        'ourguard':ourguard


    }

    return render(request,"index.html", context)
