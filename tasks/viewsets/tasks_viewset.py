
from rest_framework import viewsets
from tasks.serializers.tasks_serializer import TasksCreateSerializer

from tasks.models import Tasks

class TasksCreateQuery(viewsets.ModelViewSet):
    """ This view implements create tasks  """
    queryset = Tasks.objects.all()
    serializer_class = TasksCreateSerializer