from django.shortcuts import render
from django.http import JsonResponse
#from h11 import Data
from .models import task
from . import serealizers
from . import operations

from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
import rest_framework


def ReturnResponce(inSerealizer, notError = False, inDiscription = "Unknown ERROR"):
    if notError == True:
        return Response(inDiscription, status=rest_framework.status.HTTP_200_OK)
    else:
        return Response({
            'result': 'error',
            'discription': inDiscription,
            'InputRequest': inSerealizer.data
            }, status=rest_framework.status.HTTP_200_OK if notError == True else rest_framework.status.HTTP_400_BAD_REQUEST)


class CreateSimpleTaskCronView(APIView):
    serializer_class = serealizers.CreateSimpleTaskCronSerializer;
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            from .metods import CreateSimpleTaskCron

            appendResult = CreateSimpleTaskCron(serializer.data);
            if appendResult['result'] == True:
                return ReturnResponce(serializer, True, appendResult['data'])
            else:
                return ReturnResponce(serializer, False, appendResult['discription'])
        else:
            return ReturnResponce(serializer, False, 'Validation Error')

class StopJobViewByName(APIView):
    serializer_class = serealizers.StopJobByNameSerializer;
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            if serializer.data['id_name'] != "" and serializer.data['id_name'] != None:
                from djTaskBrocker.models import task
                taskByName = task.objects.filter(id_name=serializer.data['id_name']).first()

                if taskByName != None:
                    resultRequest = operations.stopJob(taskByName.uuid)

                    if resultRequest['result'] == True:
                        return ReturnResponce(serializer, True, 'Task with \id_name\: [' + serializer.data['id_name'] + '] was stopped successful.')
                    else:
                        return ReturnResponce(serializer, False, 'Task with \id_name\ : [' + serializer.data['id_name'] + '] was NOT stopped. ' + resultRequest['discription'])
                else:
                    return ReturnResponce(serializer, False, 'No task with "id_name": ' + request.data['id_name'])
            else:
                return ReturnResponce(serializer, False, 'No data in request')
        else:
            return ReturnResponce(serializer, False, 'Validation Error')


class StopJobViewByUUID(APIView):
    serializer_class = serealizers.StopJobByUUIDSerializer;
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()

        if 'uuid' in serializer.data:
            resultRequest = operations.stopJob(serializer.data['uuid'])

            if resultRequest['result'] == True:
                return ReturnResponce(serializer, True, 'Task with <uuid>: ' + serializer.data['uuid'] + ' stopped.')
            else:
                return ReturnResponce(serializer, False, 'Task with \id_name\ : [' + serializer.data['uuid'] + '] was NOT started. ' + resultRequest['discription'])
        else:
            return ReturnResponce(serializer, False, 'Validation Error')

class StartJobViewByName(APIView):
    serializer_class = serealizers.StopJobByNameSerializer;
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            if serializer.data['id_name'] != "" and serializer.data['id_name'] != None:
                from djTaskBrocker.models import task
                taskByName = task.objects.filter(id_name=serializer.data['id_name']).first()

                if taskByName != None:
                    
                    resultRequest = operations.startJob(taskByName.uuid)
                    
                    if resultRequest['result'] == True:
                        return ReturnResponce(serializer, True, 'Task with \id_name\: [' + serializer.data['id_name'] + '] was started successful.')
                    else:
                        return ReturnResponce(serializer, False, 'Task with \id_name\ : [' + serializer.data['id_name'] + '] was NOT started. ' + resultRequest['discription'])
                else:
                    return ReturnResponce(serializer, False, 'No task with "id_name": ' + request.data['id_name'])
            else:
                return ReturnResponce(serializer, False, 'No data in request')
        else:
            return ReturnResponce(serializer, False, 'Validation Error')

class StartJobViewByUUID(APIView):
    serializer_class = serealizers.StopJobByUUIDSerializer;
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()

        if 'uuid' in  serializer.data:
            resultRequest = operations.startJob(serializer.data['uuid'])

            if resultRequest['result'] == True:
                return ReturnResponce(serializer, True, 'Task with \id_name\ : [' + serializer.data['uuid'] + '] successfully started.')
            else:
                return ReturnResponce(serializer, False, 'Task with \id_name\ : [' + serializer.data['uuid'] + '] was NOT started. ' + resultRequest['discription'])
        else:
            return ReturnResponce(serializer, False, 'Validation Error')

class DeleteTaskViewByName(APIView):
    serializer_class = serealizers.DeleteTaskByNameSerializer;
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            if serializer.data['id_name'] != "" and serializer.data['id_name'] != None:
                from djTaskBrocker.models import task
                taskByName = task.objects.filter(id_name=serializer.data['id_name']).first()

                if taskByName != None:

                    resultRequest = operations.deleteTask(taskByName.uuid)

                    if resultRequest['result'] == True:
                        return ReturnResponce(serializer, True, 'Task with \id_name\: [' + serializer.data['id_name'] + '] was started successful.')
                    else:
                        return ReturnResponce(serializer, False, 'Task with \id_name\ : [' + serializer.data['id_name'] + '] was NOT started. ' + resultRequest['discription'])
                else:
                    return ReturnResponce(serializer, False, 'No task with "id_name": ' + request.data['id_name'])
            else:
                return ReturnResponce(serializer, False, 'No data in request')
        else:
            return ReturnResponce(serializer, False, 'Validation Error')

class DeleteTaskViewByUUID(APIView):
    serializer_class = serealizers.DeleteTaskByUUIDSerializer;
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()

        if 'uuid' in serializer.data:
            resultRequest = operations.deleteTask(serializer.data['uuid'])

            if resultRequest['result'] == True:
                return ReturnResponce(serializer, True, 'Success. Task with (uuid) : [' + serializer.data['uuid'] + '] deleted.')
            else:
                return ReturnResponce(serializer, False, 'Error. Task with (uuid) : [' + serializer.data['uuid'] + '] was NOT deleted. ' + resultRequest['discription'])
        else:
            return ReturnResponce(serializer, False, 'Validation Error')


class CreateSimpleTaskDateView(APIView):
    serializer_class = serealizers.CreateSimpleTaskDateSerializer;
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            from .metods import CreateSimpleTaskDate

            appendResult = CreateSimpleTaskDate(serializer.data);
            if appendResult['result'] == True:
                return ReturnResponce(serializer, True, appendResult['data'])
            else:
                return ReturnResponce(serializer, False, appendResult['discription'])

        else:
            return ReturnResponce(serializer, False, 'Validation Error')

class CreateSimpleTaskIntervalView(APIView):
    serializer_class = serealizers.CreateSimpleTaskIntervalSerializer;
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            from .metods import CreateSimpleTaskInterval

            appendResult = CreateSimpleTaskInterval(serializer.data);
            if appendResult['result'] == True:
                return ReturnResponce(serializer, True, appendResult['data'])
            else:
                return ReturnResponce(serializer, False, appendResult['discription'])
        else:
            return ReturnResponce(serializer, False, 'Validation Error')

class CreateTaskView(APIView):
    serializer_class = serealizers.CreateTaskSerializer;
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            from .metods import appendTask

            appendResult = appendTask(serializer.data);
            if appendResult['result'] == True:
                return ReturnResponce(serializer, True, appendResult['data'])
            else:
                return ReturnResponce(serializer, False, appendResult['discription'])
        else:
            return ReturnResponce(serializer, False, 'Validation Error')

class TaskView(generics.ListAPIView):
    queryset =  task.objects.all()
    serializer_class = serealizers.TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GetTask(APIView):
    serializer_class = serealizers.TaskSerializer
    lookup_url_kwarg = 'id_name'

    def get(self, request, format=None):
        serializer = self.serializer_class(data = request.data)
        id_name = request.GET.get(self.lookup_url_kwarg)

        if id_name != None:
            task_result = task.objects.filter(id_name=id_name)
            if len(task_result) > 0:
                data = serealizers.TaskSerializer(task_result[0]).data
                return ReturnResponce(serializer, True, data)
            return ReturnResponce(serializer, False, 'Invalid task name.')
        else:
            return ReturnResponce(serializer, False, 'Code paramater not found in request')

def getRoutes(request):

    return JsonResponse('Our API', safe=False)

# Create your views here.
