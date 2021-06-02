from django.shortcuts import render
import requests


def home(request):
    if request.method == "POST":
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;"}
        weather_request = requests.get(
            "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=-0.25",
            headers=headers)
    result = weather_request.content
    return render(request, "home/index.html", {result: result})
