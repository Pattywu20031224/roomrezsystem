from django.urls import path
from .views import *

urlpatterns = [
    path('', LogList.as_view(), name='log_list'),
    path('reserve/', ReserveTeacher.as_view(), name='reserve_teacher'), 
    path('reserve/<int:rid>/', ReserveRoom.as_view(), name='reserve_room'), 
    path('reserve/<int:rid>/<int:bid>/', ReserveLog.as_view(), name='reserve_log'),
    path('end/', EndRoom.as_view(), name='end_room'), 
    path('end/<int:lid>/', EndLog.as_view(), name='end_log'),
]