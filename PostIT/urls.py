"""PostIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='Home'),
    path("user/", include("apps.user.urls")),
    path("pedido/", include("apps.pedido.urls")),
    path("paciente/", include("apps.paciente.urls")),
    path('Login', auth.LoginView.as_view(template_name='Usuarios/login.html'), name='login'),
    path('Logout', auth.LogoutView.as_view(template_name='Usuarios/Logout.html'), name='logout'),
]
