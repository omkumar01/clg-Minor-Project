from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingPage.as_view(), name="homepage"),
    path('result', ResultsPage.as_view(), name="resultspage"),
    path("LoginRegister", LoginRegister.as_view(), name="LoginRegister"),
    path("logout", LogOut.as_view(), name="logout"),
    path("register", Register.as_view(), name="register")
]
