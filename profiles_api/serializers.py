# Add a serializer
# which is used to convert data inputs into Python objects and vice versa
# a little bit close to the function of django's form

from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our APIView """
    name = serializers.CharField(max_length = 10)


# model serilizer
class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    # this class used for validation of users' input
    class Meta:
        model = models.UserProfile
        # specify a list of filed that we want to manage through this serializer
        fields = ('id', 'email', 'name', 'password')
        # password: only valid when we want to create a new user account
        extra_kwargs = { # model configuration
            'password': {
                'write_only': True, # means password will only be valid when we input password to create a new user account
                                    # or when we want to update the password
                'style': {'input_type':'password'}
            }
        }
    # after validation, now create this user profile
    def create(self, validated_data):
        """ Create and return a new user """
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user

    # the password field requires some additional logic to hash the password before saving the update.
    #
    # Therefore, we override the Django REST Framework's update() method to add this logic to check for the presence password in the validated_data which is passed from DRF when updating an object.
    #
    # If the field exists, we will "pop" (which means assign the value and remove from the dictionary) the password from the validated data and set it using set_password() (which saves the password as a hash).
    #
    # Once that's done, we use super().update() to pass the values to the existing DRF update() method, to handle updating the remaining fields.
    def update(self, instance, validated_data):
        """ Handle updating user account """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
