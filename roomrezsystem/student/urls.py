from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentList.as_view(), name='student_list'),
    path('add/', StudentAdd.as_view(), name='student_add'),
    path('<int:pk>/', StudentView.as_view(), name='student_view'),
    path('<int:pk>/edit/', StudentEdit.as_view(), name='student_edit'),
    path('<int:pk>/delete/', StudentDelete.as_view(), name='student_delete'),
]