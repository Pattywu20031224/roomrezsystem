from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from datetime import datetime,timezone
from log.views import *

# Create your views here.

class RoomList(ListView):   
    model = Room    
    paginate_by = 8
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        logs=Log.objects.all()
        rooms=Room.objects.all()
        logdata=[]
        for log in logs:
            if log.reserve < datetime.now(timezone.utc) and log.end > datetime.now(timezone.utc) :
                logdata.append(log)
        for room in rooms:
            for logs in logdata:
                if room.id==logs.room.id:
                    room.status=0
                    room.save()
                    break
                else:
                    room.status=1
                    room.save()
        return context


class RoomView(DetailView): 
    model = Room

    ordering = ['name']    
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        logs=Log.objects.filter(room_id=self.kwargs['pk'])
        for log in logs:
            if log.end < datetime.now(timezone.utc):
                log.workstatus=0
                log.save()
            elif log.reserve > datetime.now(timezone.utc):
                log.workstatus=2
                log.save()
            elif log.reserve <= datetime.now(timezone.utc) and log.end >= datetime.now(timezone.utc) :
                log.workstatus=1
                log.save()
        context['logs']=Log.objects.order_by('-reserve').filter(room_id=self.kwargs['pk'])
        return context


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

