from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def loginGoogle(request):
    return redirect('/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatapp.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', loginGoogle, name='login-google'),
]
