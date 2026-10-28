from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Guest, Service, Booking
from django.views.generic import ListView, DetailView
from django.contrib import messages

class RoomListView(ListView):
    model = Room
    template_name = 'room_list.html'
    context_object_name = 'rooms'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        room_type = self.request.GET.get('type')
        if room_type:
            queryset = queryset.filter(room_type__icontains=room_type)
        return queryset
    


class RoomDetailView(DetailView):
    model = Room
    template_name = 'room_detail.html'
    context_object_name = 'room'

def room_list(request):
    room_type = request.GET.get('type')
    if room_type:
        rooms = Room.objects.filter(room_type__icontains=room_type)
    else:
       rooms = Room.objects.all()
       
    return render(request, 'room_list.html', {'rooms':rooms})


def detail_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'room_detail.html', {'room': room})

def booking_create(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        fio =  request.POST.get('guest_fio')
        passport = request.POST.get('guest_passport')
        date_in = request.POST.get('date_ind').split('T')[0]
        date_out = request.POST.get('date_outd').split('T')[0]
    
        room = get_object_or_404(Room, id=room_id)
    
        guest, created = Guest.objects.get_or_create(
            passport = passport,
            defaults={'fio':fio},
        )
    
        Booking.objects.create(
            room = room,
            guest = guest, 
            date_arrival = date_in,
            date_departure = date_out
        )
        
        messages.success(request, f'Бронь для {fio} на номер {room.number} успешно создана')
    
        return redirect('hotel:room_list')
    
    rooms = Room.objects.all()
    return render(request, 'booking_create.html', {'rooms': rooms} )

