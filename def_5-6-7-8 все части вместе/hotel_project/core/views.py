from django.shortcuts import render
from django.views.generic import ListView
from hotel_def.models import Room 

def home(request):
    return render(request, 'home.html')

class ListViewsStats(ListView):
    model = Room 
    template_name = 'stats.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        return super().get_queryset()