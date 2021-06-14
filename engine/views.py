from django.http import HttpResponse
from django.shortcuts import render
from .models import Url
from django.views.generic import View
from django.contrib.auth import authenticate, login


class LoginRegister(View):

    def get(self, request):
        return render(request, 'LoginRegister.html', {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        # print("email =", username)
        # print("password = ", password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.user = user
            return HttpResponse("success")
        else:
            return HttpResponse("no user")


class LandingPage(View):

    def get(self, request):
        if request.method == 'POST':
            link = request.POST['link']
            print(link)
        return render(request, "index.html", {})


class ResultsPage(View):

    def post(self, request):
        if request.method == 'POST':
            link = request.POST['link']
            print(link)
            data = Url.objects.filter(input_link=link)
            print(data)
            if data == None:
                db = Url(input_link=link)
                db.save()
            content = {}
            content['data'] = {
                'link': link,
            }
        return render(request, 'index.html', content)
