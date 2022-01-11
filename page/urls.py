from django.urls import path
from page import views

app_name = 'page'
urlpatterns = [
    path('', views.homepage, name='homepage')
]
