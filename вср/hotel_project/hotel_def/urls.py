from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    path('rooms/', views.RoomListView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
    path('bookings/create/', views.booking_create, name='booking_create'),
    
]