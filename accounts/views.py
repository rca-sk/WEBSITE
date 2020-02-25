from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # chech if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username taken')
            return redirect('register')

        # chech if email is already registered
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('register')

        # chech if passwords do not match
        elif password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        # if everything is fine,
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
            user.save()
            # send user to login page
            return redirect('login')
            # or use: auth.login(request, user) to log in the user directly after registration

    # if the request is GET
    else:
        return render(request, 'registration.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # if credentials are correct authenticate user
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')

    # for a GET request
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
