from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def Subscription(request):
    return render(request, 'Subscription.html')


def Library(request):
    return render(request, 'Library.html')



from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('login')



@login_required
def update_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        email = request.POST.get('email')
        current_password = request.POST.get('current_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if email:
            user.email = email
            user.save()

        if current_password and new_password1 and new_password2:
            if not user.check_password(current_password):
                return render(request, 'update_profile.html', {'user': user, 'error': 'Current password is incorrect'})
            if new_password1 != new_password2:
                return render(request, 'update_profile.html', {'user': user, 'error': 'New passwords do not match'})
            user.set_password(new_password1)
            user.save()
            update_session_auth_hash(request, user)  # Keeps the user logged in after password change
            return redirect('home')

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
