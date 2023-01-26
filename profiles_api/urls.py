# url for our api
from django.urls import path, include

from rest_framework.routers import DefaultRouter
# Router automatically maps the incoming request to proper viewset action based on the request method type

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name='hello-viewset') # register URL prefix we defined
                                                    # then register viewset we defined in views.py
                                                    # then specify the base name for our viewset


# create new list variable
urlpatterns = [
    # as_view: standard method to convert api view class to be rendered by our urls
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)), # why empty string
                                # because we want to include all url patterns in router
]
