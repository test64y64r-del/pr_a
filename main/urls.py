from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('col1/', views.col1_view, name='col1'),
    path('col2/', views.col2_view, name='col2'),
    path('col3/', views.col3_view, name='col3'),
]