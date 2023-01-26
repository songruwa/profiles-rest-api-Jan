# url for our api
from django.urls import path

from profiles_api import views

# create new list variable
urlpatterns = [
    # as_view: standard method to convert api view class to be rendered by our urls
    path('hello-view/', views.HelloApiView.as_view()),


]
