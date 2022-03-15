from typing_extensions import Self
from django.urls import reverse
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from teacher.models import Teacher
from room.models import Room
from .models import Log
from django.shortcuts import render,redirect

# 借閱記錄列表
class LogList(LoginRequiredMixin, ListView):
    model = Log
    ordering = ['-reserve']
    
class ReserveTeacher(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'log/reserve_teacher_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            teachers = Teacher.objects.filter(realname__icontains=query)
        else:
            teachers = Teacher.objects
        return teachers.order_by('realname')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('query') or ""
        return ctx
class ReserveRoom(LoginRequiredMixin, ListView):
    model = Room
    template_name = 'log/reserve_room_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            rooms = Room.objects.filter(name__icontains=query)
        else:
            rooms = Room.objects
        return rooms.exclude(
            log__reserve__isnull=False, 
            log__end__isnull=True
        ).order_by('name')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        curr_teacher = Teacher.objects.get(id=self.kwargs['rid'])
        ctx['query'] = self.request.GET.get('query') or ""
        ctx['teacher'] = curr_teacher
        ctx['reserving'] = curr_teacher.log_set.filter(
            end__isnull=True
        ).select_related('room')
        return ctx
class ReserveLog(LoginRequiredMixin, RedirectView):
    def room_status(self,**kwargs):
        room=Room.objects.filter(id=self.kwargs['rid'])
        ch_room=room[0]
        ch_room.delete
    def get_redirect_url(self, **kwargs):
        teacher = Teacher.objects.filter(id=self.kwargs['tid'])
        ch_teacher = teacher[0]
        room = Room.objects.filter(id=self.kwargs['rid'])
        ch_room=room[0]
        for rooms in room:
            rooms.status=0
            rooms.save()
        log = Log(teacher=ch_teacher, room=ch_room)
        log.save()
        #return reverse('roomstatus', kwargs={'rid': ch_room.id,'sid':ch_room.status})
        return reverse('log_list')

'''def RoomStatus(request,rid,sid):
    room=Room.objects.filter(id=rid)
    ch_room=room[0]
    if sid == 0:
        ch_room.status=1
    else:
        ch_room.status=0

    return redirect(reverse('log_list'))'''


#############################################################

class EndRoom(LoginRequiredMixin, ListView):
    model = Log
    template_name = 'log/end_room_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            logs = Log.objects.filter(room__name__icontains=query)
        else:
            logs = Log.objects
        return logs.exclude(
            end__isnull=False
        ).select_related('room', 'teacher')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('query') or ""
        return ctx
        
class EndLog(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        log = Log.objects.get(id=self.kwargs['lid'])
        rooms=Room.objects.filter(id=log.room_id)
        for room in rooms:
            room.status=1
            room.save()
        log.end = datetime.now()
        log.save()
        return reverse('log_list')

