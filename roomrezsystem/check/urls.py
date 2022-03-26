from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path('',views.CheckForm),
    path('submit.php',views.Check)
]