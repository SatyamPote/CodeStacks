from django.contrib import admin
from django.urls import path
from Base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registation/', views.registation, name='registation'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('update_profile/<int:user_id>/', views.update_profile, name='update_profile'),
    path('logout/', views.logout, name='logout'),
]
