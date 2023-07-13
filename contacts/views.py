from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.


def contact(request):
    if request.method == 'POST':
        context = {
            'listing': request.POST['listing'],
            'listing_id': request.POST['listing_id'],
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'message': request.POST['message'],
            'user_id': request.POST['user_id'],
        }

        contact = Contact.objects.create(**context)
        contact.save()

        return redirect('/listings/' + context["listing_id"])
