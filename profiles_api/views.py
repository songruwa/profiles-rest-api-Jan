from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """ Test API View """
    # define application logic of this view

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
