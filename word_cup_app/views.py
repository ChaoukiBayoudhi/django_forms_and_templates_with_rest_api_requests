from django.shortcuts import render

# Create your views here.
import requests
def index(request):
    matches = requests.get('http://worldcup.sfg.io/matches')
    #matches = response.json()
    return render(request, 'index.html', {'matches': matches})

