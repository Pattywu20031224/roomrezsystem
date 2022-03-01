from django.urls import path
from .views import *

urlpatterns = [
    path('', RoomList.as_view(), name='room_list'),
    path('add/', RoomAdd.as_view(), name='room_add'), 
    path('<int:pk>/', RoomView.as_view(), name='room_view'),
    path('<int:pk>/edit/', RoomEdit.as_view(), name='room_edit'),
    path('<int:pk>/delete/', RoomDelete.as_view(), name='room_delete'),
]
