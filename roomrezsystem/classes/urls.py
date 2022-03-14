from django import views
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', ClassesList.as_view(), name='classes_list'),
    path('add/', ClassesAdd.as_view(), name='classes_add'), 
    path('<int:pk>/stu_relate',ClassesRelateStudentList.as_view(),name='classes_stu_relate'),
    path('<int:pk>/tea_relate',ClassesRelateTeacherList.as_view(),name='classes_tea_relate'),
    path('<int:pk>/stu_relate/<int:stu>', views.ClassesManytomanyForStudent,name='classes_relate_student'),
    path('<int:pk>/tea_relate/<int:tea>', views.ClassesManytomanyForTeacher,name='classes_relate_teacher'),
    path('<int:pk>/', ClassesView.as_view(), name='classes_view'),
    path('<int:pk>/edit/', ClassesEdit.as_view(), name='classes_edit'),
    path('<int:pk>/delete/', ClassesDelete.as_view(), name='classes_delete'),
]