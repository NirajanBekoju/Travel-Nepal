from django.shortcuts import render, redirect, Http404
from django.contrib import messages, auth
from .models import Account

def register(request):
    if request.method == 'POST':
        # Get Form Values
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        print(first_name, last_name, email)
        if (password == password2):
            if Account.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Taken') 
                return redirect('register')
            else:
                if Account.objects.filter(email=email).exists():
                    messages.error(request, 'Email Already Taken') 
                    return redirect('register')
                else:
                    # Everything fine
                    user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'you are now logged in)
                    # return redirect('index')
                    user.save()
                    messages.success(request, "You are now registered...")
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')

        return redirect('register')
    # if GET request
    else:
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'accounts/register.html')
        

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'pages/index.html')
    raise Http404   