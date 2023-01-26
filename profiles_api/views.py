from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # is a list of HTTP status codes that used when returning responses from API
from rest_framework import viewsets
# use status in Post function
from profiles_api import serializers # used to tell APIView what kind of data to expect when make post and patch data

from profiles_api import models

# Create your views here.
class HelloApiView(APIView):
    """ Test API View """
    # define application logic of this view

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features """
        # request: passed by Django Framework, and contains
        # details of the request being made to the API

        # format: used to add a format suffic to the end of the endpoint URL

        # GET function here: define a list which describes all of the features
        # of an API view
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        # Response needs to contain a list or a dictionary
        # When Api is called, it will converts the response object into JSON
        # in order to convert into json, it needs to be list or dict
        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)
        # serializer_class: a function come from APIView
        # used to retrieve the configured serializer class for our view

        # now validate serializer
        # validate the name is no longer than 10
        if serializer.is_valid():
            # retrieve the name field from validated data
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            # if input doesn't pass serializer's validation, it will generate error message
            # serializer.errors: will output all error messages
            # Response(serializer.errors): originally will output Http200

            # now we want it to output Http400
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST)
                # The 4xx class of status code is intended for cases in which the client seems to have errors


    # used to update an object
    # put, primarily deal with primary key
    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'method': 'PUT'})

    def patch(self,request, pk=None):
        """ Handle a partial update of an object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a Hello message """
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})


    def create(self, request):
        """ Create a new hello message """
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    # retrieve a specific object in our viewset
    def retrieve(self, request, pk = None):
        """ Handle getting an object by its ID """
        return Response({'http_method':'GET'})

    def update(self, request, pk = None):
        """ Handle updating an object """
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk = None):
        """ Handle updating part of an object """
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk = None):
        """ Handle Removing an object"""
        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all() # 
