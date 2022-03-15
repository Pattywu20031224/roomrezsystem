from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path('', LogList.as_view(), name='log_list'),
    path('reserve/', ReserveTeacher.as_view(), name='reserve_teacher'), 
    #path('reserve/<int:rid>/', ReserveRoom.as_view(), name='reserve_room'), 
    path('reserve/<int:tid>/<int:rid>/', ReserveLog.as_view(), name='reserve_log'),
    path('reverseroom/<int:rid>', Reverseroom.as_view(),name='reverse_room'),
    path('end/', EndRoom.as_view(), name='end_room'), 
    path('end/<int:lid>/', EndLog.as_view(), name='end_log'),
]