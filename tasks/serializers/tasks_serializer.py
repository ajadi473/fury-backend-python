from rest_framework import serializers
from tasks.models import Tasks
from django.utils import timezone

# class TasksCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tasks
#         fields = "__all__"