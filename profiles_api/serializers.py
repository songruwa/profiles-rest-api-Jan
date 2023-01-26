# Add a serializer
# which is used to convert data inputs into Python objects and vice versa
# a little bit close to the function of django's form

from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our APIView """
    name = serializers.CharField(max_length = 10)
    
