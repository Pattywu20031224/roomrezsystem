from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from student.models import *

# Create your views here.

class ClassesList(LoginRequiredMixin, ListView):   
    model = Classes    
    paginate_by = 20


class ClassesView(LoginRequiredMixin, DetailView): 
    model = Classes

    ordering = ['name']    
    paginate_by = 20
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        student_list = Student.objects.filter(classes=self.kwargs['pk'])
        context['student_list']=student_list
        return context

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
