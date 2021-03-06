"""mysite URL Configuration

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
from django.urls import path, include
from photo import views


app_name ='photo'
urlpatterns = [
    path('', views.AlbumLV.as_view(), name='index'),
    path('album', views.AlbumLV.as_view(), name='album_list'),
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),
    path('photo/<int:pk>', views.PhotoDV.as_view(), name='photo_detail'),
    ]
