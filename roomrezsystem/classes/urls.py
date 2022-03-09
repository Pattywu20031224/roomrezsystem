from django.urls import path
from .views import *

urlpatterns = [
    path('', ClassesList.as_view(), name='classes_list'),
    path('add/', ClassesAdd.as_view(), name='classes_add'), 
    path('<int:pk>/', ClassesView.as_view(), name='classes_view'),
    path('<int:pk>/edit/', ClassesEdit.as_view(), name='classes_edit'),
    path('<int:pk>/delete/', ClassesDelete.as_view(), name='classes_delete'),
]