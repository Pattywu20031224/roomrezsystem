from urllib import request
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from student.models import *
from django.db import *
from teacher.models import *

# Create your views here.

class ClassesList(LoginRequiredMixin, ListView):   
    model = Classes    
    paginate_by = 20


class ClassesView(LoginRequiredMixin, DetailView): 
    model = Classes

    ordering = ['name']    
    paginate_by = 20
    
    def get_queryset(self):
        return Classes.objects.prefetch_related('student_set','teacher_set')
        

class ClassesAdd(LoginRequiredMixin, CreateView):  
    model = Classes
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('classes_list')

class ClassesEdit(LoginRequiredMixin, UpdateView): 
    model = Classes
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('classes_list')

class ClassesDelete(LoginRequiredMixin, DeleteView):   
    model = Classes
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('classes_list')

class ClassesRelateStudentList(LoginRequiredMixin,ListView):
    model= Student
    template_name = 'classes/stu_relate.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        classes=Classes.objects.filter(id=self.kwargs['pk'])
        context['choosen_classes']=classes[0]
        return context

class ClassesRelateTeacherList(LoginRequiredMixin,ListView):
    model= Teacher
    template_name = 'classes/tea_relate.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        classes=Classes.objects.filter(id=self.kwargs['pk'])
        context['choosen_classes']=classes[0]
        return context


def ClassesManytomanyForStudent(reqeust,pk,stu):

    choosen_students=Student.objects.get(id=stu)
    choosen_classes=Classes.objects.get(id=pk)
    choosen_students.stu_classes.add(choosen_classes)
    #choosen_class=Classes
    #choosen_students=Student(realname='gg',cardid='123')
    #choosen_students.save()
    #choosen_student=Student.objects.filter(id=stu).classes.add(choosen_classes)
    #for choosen_student in choosen_students:
        #choosen_student.stu_classes.add(choosen_classes[0])
    #for choosen_student in choosen_students:
        
    return redirect(reverse('classes_view',args=str(pk)))

def ClassesManytomanyForTeacher(reqeust,pk,tea):

    choosen_teachers=Teacher.objects.get(id=tea)
    choosen_classes=Classes.objects.get(id=pk)
    choosen_teachers.tea_classes.add(choosen_classes)
    #choosen_class=Classes
    #choosen_teacher=Teacher(realname='hentai',cardid='6969')
    #choosen_teacher.save()
    #choosen_class=choosen_classes[0]
    #choosen_teacher.classes.add(choosen_class)
    #choosen_student=Student.objects.filter(id=stu).classes.add(choosen_classes)
    #for choosen_teacher in choosen_teachers:
        #choosen_teacher.classes.set(choosen_classes)
        #choosen_teacher.tea_classes.add(choosen_classes[0])
    #for choosen_student in choosen_students:
        
    return redirect(reverse('classes_view',args=str(pk)))