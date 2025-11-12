from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notebooks/', views.notebooks, name='notebooks'),
    path('office/', views.office, name='office'),
    path('self-development/', views.self_development, name='self_development'),
    path('digital/', views.digital, name='digital'),
]
