from django.shortcuts import render
# Create your views here.
import python_weather
from  ..models.models import A
import asyncio
import os


async def getweather(location):
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        # fetch a weather forecast from a city
        weather = await client.get(location)
        return (weather.current.temperature-32)*5/9

        # returns the current day's forecast temperature (int)
        # print(weather.current.temperature)

        # # get the weather forecast for a few days
        # for forecast in weather.forecasts:
        #     print(forecast)
        #
        #     # hourly forecasts
        #     for hourly in forecast.hourly:
        #         print(f' --> {hourly!r}')
def homepage(request):
    print(request.POST)
    try:
        a = int(request.POST['num1'])
        b = int(request.POST['num2'])
    except:
        a=b=0
    location = list(request.POST.get('location')) or ['Tashkent']
    print(f'<{location}>')
    t = asyncio.run(getweather(''.join(location)))
    print(f't = {t}, {type(t)}')
    # # print(request.POST)
    return render(request, 'app1/index.html',{'a':a,'b':b,'c':a+b,'temp':t,'location':''.join(location)})
    # return render(request, 'app1/index.html')
