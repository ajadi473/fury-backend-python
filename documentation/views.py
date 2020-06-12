
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Django
from django.shortcuts import render
from django.contrib.auth.models import User

# Documentation App
from documentation.serializer import EndpointSerializer
from documentation.models import Endpoint

# Provider OAuth2



from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import   api_view, renderer_classes
from rest_framework import schemas





class Endpoint_view(viewsets.ModelViewSet):
   
    """ This endpoint returns a list of all the endpoints and their related data.
    This endpoint also allows authenticated users to add documentation for a new endpoints"""

    queryset = Endpoint.objects.all()
    serializer_class = EndpointSerializer
    
    


