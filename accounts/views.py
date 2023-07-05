from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        pwd_2 = request.POST['password2']

        # Check passwords
        if pwd == pwd_2:
            e_mail = User.objects.filter(email=email).exists()
            user_name = User.objects.filter(username=username).exists()
            objects = {
                'email': e_mail,
                'username': user_name
            }

            # Check email and username
            for key, val in objects.items():
                if val is True:
                    messages.add_message(request, messages.ERROR, f'This {key} already exist')
                    return redirect('register')

            # Create user if OK
            user = User.objects.create_user(
                username=username, password=pwd, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.add_message(request, messages.SUCCESS, f'Welcome to BT Real Estate')
            return redirect('login')

        else:
            messages.add_message(request, messages.ERROR, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
