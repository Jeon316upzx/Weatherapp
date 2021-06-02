from django.shortcuts import render
import requests


def home(request):
    cxt = {}
    if request.method == "POST":
        lattitude = request.POST['lat']
        long = request.POST['long']
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;"}
        weather_request = requests.get(
            "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}".format(
                lattitude, long),
            headers=headers)
        print(weather_request.content)
        cxt = {
            "results": weather_request.content
        }
    else:
        cxt = {}
    return render(request, "home/index.html", cxt)
