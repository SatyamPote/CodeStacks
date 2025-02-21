from django.contrib import admin
from django.urls import path
from Base import views  # Ensure 'Base' is the correct app name
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registation/', views.registation, name='registation'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('update_profile/<int:user_id>/', views.update_profile, name='update_profile'),
    path('logout/', views.logout, name='logout'),
    path('Subscription/', views.Subscription, name='Subscription'),
    path('Library/', views.Library, name='Library'),
    path('Collection/', views.Collection, name='Collection'),
    path('Support/', views.Support, name='Support'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = TemplateView.as_view(template_name='404.html')
