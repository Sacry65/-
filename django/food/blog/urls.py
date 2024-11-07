from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pasta/', views.pasta, name='pasta'),
    path('salat/', views.salat, name='salat'),
    path('soup/', views.soup, name='soup'),
]