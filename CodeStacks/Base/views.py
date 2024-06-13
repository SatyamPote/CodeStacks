from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    return render(request, 'home.html')

from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('login')



@login_required
def update_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            user.email = email
            user.save()
            return redirect('home')
    return render(request, 'update_profile.html', {'user': user})


def registation(request):
    if request.method == 'POST':
        username1 = request.POST.get('username1')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'registation.html', {'error': "Passwords don't match"})
        elif User.objects.filter(username=username1).exists():
            return render(request, 'registation.html', {'error': "Username already exists"})
        elif User.objects.filter(email=email).exists():
            return render(request, 'registation.html', {'error': "Email already exists"})
        else:
            my_user = User.objects.create_user(username=username1, email=email, password=password1)
            my_user.save()
            return redirect('login')

    return render(request, 'registation.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': "Invalid username or password"})

    return render(request, 'login.html')
