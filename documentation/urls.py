from rest_framework import routers
from django.urls import path, include
from documentation.views import Endpoint_view
app_name= "Documentation"
router = routers.DefaultRouter()
router.register('', Endpoint_view)
urlpatterns = router.urls


