from django.contrib import admin
from django.urls import path
from engine.views import LandingPage, ResultsPage, LoginRegister

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name="homepage"),
    path('result', ResultsPage.as_view(), name="resultspage"),
    path("LoginRegister", LoginRegister.as_view(), name="LoginRegister")
]
