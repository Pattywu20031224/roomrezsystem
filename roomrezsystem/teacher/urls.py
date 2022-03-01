from django.urls import path
from .views import *

urlpatterns = [
    path('', TeacherList.as_view(), name='teacher_list'), 
    path('add/', TeacherAdd.as_view(), name='teacher_add'),
    path('<int:pk>/', TeacherView.as_view(), name='teacher_view'), 
    path('<int:pk>/edit/', TeacherEdit.as_view(), name='teacher_edit'),
    path('<int:pk>/delete/', TeacherDelete.as_view(), name='teacher_delete'),
]