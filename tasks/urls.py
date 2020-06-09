from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url

from tasks.viewsets.tasks_viewset import TasksCreateQuery
app_name = "team_fury_tasks"

router = routers.DefaultRouter()

router.register('tasks', TasksCreateQuery)

urlpatterns = router.urls
