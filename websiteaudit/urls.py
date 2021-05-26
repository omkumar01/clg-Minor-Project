from django.contrib import admin
from django.urls import path
from engine.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ),
    path('result', result),
]
