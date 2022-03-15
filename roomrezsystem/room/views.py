from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from datetime import datetime

# Create your views here.

class RoomList(LoginRequiredMixin, ListView):   
    model = Room    
    paginate_by = 8


class RoomView(LoginRequiredMixin, DetailView): 
    model = Room

    ordering = ['name']    
    paginate_by = 20

    

class RoomAdd(LoginRequiredMixin, CreateView):  
    model = Room
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('room_list')

class RoomEdit(LoginRequiredMixin, UpdateView): 
    model = Room
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('room_list')

class RoomDelete(LoginRequiredMixin, DeleteView):   
    model = Room
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('room_list')

