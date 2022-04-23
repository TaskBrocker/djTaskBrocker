from attr import field
from rest_framework import serializers
from .models import task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ('name', 'id_name')

class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ('name', 'id_name')
