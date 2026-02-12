
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),  # همه‌چیز از main می‌آید
]
