from django.shortcuts import render
from django.http import JsonResponse
from h11 import Data
from .models import task
from . import serealizers

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
import rest_framework

class CreateTaskView(APIView):
    serializer_class = serealizers.CreateTaskSerializer;

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            id_name = serializer.data.get("id_name");
            name = serializer.data.get("name");

            newTask = task(id_name=id_name, name=name, trigger_type="sdfsdf", task_app_name="sdfsdf", task_module_name="dsfsdf", task_function_name="sdf3wew", execute=False)
            newTask.save();

            return Response(serealizers.TaskSerializer(newTask).data, status=rest_framework.status.HTTP_200_OK)
        else:
            return Response({'Bad Request': 'Brocken data'}, status=rest_framework.status.HTTP_400_BAD_REQUEST)


class TaskView(generics.ListAPIView):
    queryset =  task.objects.all()
    serializer_class = serealizers.TaskSerializer

class GetTask(APIView):
    serializer_class = serealizers.TaskSerializer
    lookup_url_kwarg = 'id_name'

    def get(self, request, format=None):
        id_name = request.GET.get(self.lookup_url_kwarg)
        if id_name != None:
            task_result = task.objects.filter(id_name=id_name)
            if len(task_result) > 0:
                data = serealizers.TaskSerializer(task_result[0]).data
                #data['is_host'] = self.request.session.session_key == room[0].host
                return Response(data, status=rest_framework.status.HTTP_200_OK)
            return Response({'Room Not Found': 'Invalid task name.'}, status=rest_framework.status.HTTP_404_NOT_FOUND)

        return Response({'Bad Request': 'Code paramater not found in request'}, status=rest_framework.status.HTTP_400_BAD_REQUEST)


def getRoutes(request):

    return JsonResponse('Our API', safe=False)

# Create your views here.
