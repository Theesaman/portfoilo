from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.

def home_view(request):
    return render(request,'home.html')

def contact_view(request):
    if request.method == "POST":
        try:
            name = (request.POST.get('name'))
            email = (request.POST.get('email'))
            content = (request.POST.get('content'))
            new_contact = Contact(name=name,email=email,content=content)
            new_contact.save()
            messages.success(request, "Xabar yuborildi !")
            return HttpResponseRedirect(reverse('home-page'))
        except:
            pass

    return render(request,'contact.html')