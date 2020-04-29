import requests
from django.shortcuts import render


def home(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()
    return render(request, "main_app/home.html", {"data": todos})
