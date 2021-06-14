from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Url
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class LoginRegister(View):

    """ Handles Login Page """

    def get(self, request):

        return render(request, 'LoginRegister.html', {})

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']
        u = authenticate(request, username=username, password=password)
        if u is not None:
            login(request, u)
            print("user logged in")
            return redirect("/")
        else:
            return render(request, 'LoginRegister.html', {"login": False})


class LogOut(LoginRegister):

    """ Class Inherited from LoginRegister Class perform User Registration """

    def get(self, request):

        logout(request)
        return redirect('/LoginRegister')


class Register(LoginRegister):

    """ Class Inherited from LoginRegister Class perform User Registration """

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['email']
        password = request.POST['password']

        try:
            add_user = User.objects.create_user(
                first_name=name, username=username, email=email, password=password, is_superuser=False)
            add_user.save()
        except:
            return redirect("login")

        return HttpResponse("success")


class LandingPage(LoginRequiredMixin, View):

    """A Class for just landing Page rendering"""

    def get(self, request):

        return render(request, "index.html", {})


class ResultsPage(LoginRequiredMixin, View):

    """ This Class will be making a Request to Generate Data and render Result Template """

    def post(self, request):

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
