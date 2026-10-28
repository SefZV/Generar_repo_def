import json
from django.shortcuts import render
from django.views.generic import ListView
from hotel_def.models import Room 
from urllib.request import urlopen

def home(request):
    return render(request, 'home.html')

class ListViewsStats(ListView):
    model = Room 
    template_name = 'stats.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        return super().get_queryset()




def currency_view(request):
    try:
        response = urlopen('https://www.cbr-xml-daily.ru/daily_json.js')
        data = json.loads(response.read())
        usd = data['Valute']['USD']['Value']
        eur = data['Valute']['EUR']['Value']
        error = None
    except Exception as e:
        usd = None
        eur = None
        error = "Не удалось загрузить данные"
    return render(request, 'currency.html', {'usd': usd, 'eur': eur, 'error': error})




def weather_view(request):
    try: 
        response = urlopen('https://wttr.in/Abakan?format=j1')
        data = json.loads(response.read())
        
       
        temp_c = data['current_condition'][0]['temp_C']
        desc = data['current_condition'][0]['weatherDesc'][0]['value']
        
        error = None
    except Exception as e:
        temp_c = None
        desc = None
        error = "Не удалось загрузить данные о погоде"

    return render(request, 'weather.html', {
        'temp': temp_c,
        'desc': desc,
        'error': error
    })