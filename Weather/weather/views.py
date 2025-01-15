# weather/views.py
import requests # type: ignore
from django.shortcuts import render # type: ignore

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'eaf74fe7a0022dfc5051ccf8e16f2aa6'  
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data = {'error': 'City not found'}
        
        return render(request, 'weather/index.html', {'weather': weather_data})

    return render(request, 'weather/index.html')
