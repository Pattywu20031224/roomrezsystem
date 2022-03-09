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

class StudentAdd(LoginRequiredMixin, CreateView):  
    model = Student
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('student_list')

class StudentEdit(LoginRequiredMixin, UpdateView): 
    model = Student
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('student_list')

class StudentDelete(LoginRequiredMixin, DeleteView):   
    model = Student
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('student_list')

