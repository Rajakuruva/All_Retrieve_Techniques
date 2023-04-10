"""Backup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Data_Topic/',Data_Topic,name='Data_Topic'),
    path('Data_Webpage/',Data_Webpage,name='Data_Webpage'),
    path('Data_AccessRecord/',Data_AccessRecord,name='Data_AccessRecord'),
    path('Update_Webpage/',Update_Webpage,name='Update_Webpage'),
    path('Update_or_create_Webpage/',Update_or_create_Webpage,name='Update_or_create_Webpage'),
]
