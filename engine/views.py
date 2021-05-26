from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Url

def index(request):
    if request.method =='POST':
        link = request.POST['link']
        print(link)

    return render(request, "index.html", {})

def result(request):
    if request.method =='POST':
        link = request.POST['link']
        print(link)
        db = Url(input_link=link)
        db.save()
        content= {}
        content['data'] = {
            'link':link,
        }
    return render(request, 'index.html', content )