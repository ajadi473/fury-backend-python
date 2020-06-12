from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User
from documentation.models import Endpoint


class EndpointSerializer(serializers.HyperlinkedModelSerializer):

    """ This serializes and serializes and Endpoint object """

    class Meta:
        model = Endpoint
        fields= "__all__"