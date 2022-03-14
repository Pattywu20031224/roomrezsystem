from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

# Create your views here.
class TeacherList(LoginRequiredMixin, ListView):    
    model = Teacher
    ordering = ['realname']    
    paginate_by = 20

class TeacherView(LoginRequiredMixin, DetailView):   
    model = Teacher

class TeacherAdd(LoginRequiredMixin, CreateView):    
    model = Teacher
    fields = 'realname','tel','role','cardid'
    template_name = 'form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherEdit(LoginRequiredMixin, UpdateView):   
    model = Teacher
    fields = 'realname','tel','role','cardid'
    template_name = 'form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherDelete(LoginRequiredMixin, DeleteView): 
    model = Teacher
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('teacher_list')