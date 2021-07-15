from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Url
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .scrapbot import onPage


class LoginRegister(View):
    """Handles Login Page"""

    def get(self, request):

        return render(request, "LoginRegister.html", {})

    def post(self, request):
        content = {}
        username = request.POST["username"]
        password = request.POST["password"]
        u = authenticate(request, username=username, password=password)
        print("u = ", u)
        if u is not None:
            login(request, u)
            print("user logged in")
            return redirect("/")
        else:
            content = {
                "login": False,
                "message": "Invalid username or password",
            }
            print("login failed")
            return render(request, "LoginRegister.html", content)


class LogOut(LoginRegister):
    """Class Inherited from LoginRegister Class perform User Registration"""

    def get(self, request):

        logout(request)
        return redirect("/LoginRegister")


class ChangePassword(View):
    def get(self, request):
        return render(request, "changePassword.html")

    def post(self, request):
        content = {}
        if request.POST["username"]:
            username = request.POST["username"]
            user = User.objects.get(username=username)
            if user is None:
                content["message"] = "User Not found"
                return render(request, "changePassword.html", content)
            else:
                content["user"] = username
                return render(request, "changePassword.html", content)

        username = request.POST["name"]
        password = request.POST["password"]
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        return HttpResponse("success")


class Register(LoginRegister):
    """Class Inherited from LoginRegister Class perform User Registration"""

    def post(self, request):
        name = request.POST["name"]
        email = request.POST["email"]
        username = request.POST["email"]
        password = request.POST["password"]

        try:
            add_user = User.objects.create_user(
                first_name=name,
                username=username,
                email=email,
                password=password,
                is_superuser=False,
                is_active=False,
            )
            add_user.save()
        except:
            return HttpResponse("User Registration failed")

        return HttpResponse("Verify your email before procceding")


class LandingPage(LoginRequiredMixin, View):
    """A Class for just landing Page rendering"""

    def get(self, request):

        return render(request, "index.html", {})


class ResultsPage(LoginRequiredMixin, View):
    """This Class will be making a Request to Generate Data and render Result Template"""

    def post(self, request):
        content = {}
        link = request.POST["link"]
        data = onPage(link)
        content["data"] = data

        db = Url()
        db.input_link = link
        db.onpagedata = data
        db.save()

        # for i, j in data.items():
        #     print(i)

        content["link"] = link

        return render(request, "index.html", content)
