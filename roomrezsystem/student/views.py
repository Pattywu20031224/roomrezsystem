from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

# Create your views here.

class StudentList(LoginRequiredMixin, ListView):   
    model = Student    
    paginate_by = 20


class StudentView(LoginRequiredMixin, DetailView): 
    model = Student

    ordering = ['name']    
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        classes=Student.objects.filter(id=self.kwargs['pk'])
        stu_classes=classes[0]
        context['stu_classes']=stu_classes.stu_classes.all
        return context

class StudentAdd(LoginRequiredMixin, CreateView):  
    model = Student
    fields = 'realname','cardid'
    template_name = 'form.html'
    success_url = reverse_lazy('student_list')

class StudentEdit(LoginRequiredMixin, UpdateView): 
    model = Student
    fields = 'realname','cardid'
    template_name = 'form.html'
    success_url = reverse_lazy('student_list')

class StudentDelete(LoginRequiredMixin, DeleteView):   
    model = Student
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('student_list')

