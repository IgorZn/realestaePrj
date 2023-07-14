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

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=context['listing_id'], user_id=context[user_id])
            if has_contacted:
                messages.add_message(request, messages.ERROR, f'You have already made an inquiry for this listing')
            else:
                contact = Contact.objects.create(**context)
                contact.save()

                messages.add_message(request, messages.SUCCESS, f'Your request has been submitted.')

        return redirect('/listings/' + context["listing_id"])
