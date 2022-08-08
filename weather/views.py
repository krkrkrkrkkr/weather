from django.shortcuts import render, redirect
import requests as req
import json
from .models import City

# Create your views here.
def home(requests):
    if requests.method=="POST":
        city_name=requests.POST['place']
        City(name=city_name).save()
    cities=City.objects.all()
    weather_data=[]
    for city in cities:
        place = city
        api_key="e859b26ce54db305e980244ab4012174"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&units=metric&appid={api_key}"
        data = req.get(url).json()
        temp=data['main']['temp']
        desc=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        city_weather = {"city":place.name, 'temperature':temp, 'description':desc, 'icon':icon}
        weather_data.append(city_weather)

    context={"data":weather_data}
    return render(requests, 'weather.html', context)

def delete(request, name):
    a=City.objects.filter(name=name).delete()
    print(a)
    return redirect('home')
