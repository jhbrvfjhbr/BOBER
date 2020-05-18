from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name= 'home'),
    ]
urlpatterns += [
    path('pudge', pudge, name= 'pudge'),
    ]