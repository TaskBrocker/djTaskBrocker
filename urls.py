from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.getRoutes, name="routes"),
    path('get-list', views.TaskView.as_view())
    #,path('create-task', views.CreateTaskView.as_view())
    ,path('create-task-interval', views.CreateSimpleTaskIntervalView.as_view())
    #,path('create-task-cron', views.CreateSimpleTaskCronView.as_view())
    #,path('create-task-date', views.CreateSimpleTaskDateView.as_view())
    ,path('stop-job-by-name', views.StopJobViewByName.as_view())
    ,path('stop-job-by-uuid', views.StopJobViewByUUID.as_view())
    ,path('start-job-by-name', views.StartJobViewByName.as_view())
    ,path('start-job-by-uuid', views.StartJobViewByUUID.as_view())
    ,path('delete-task-job-by-name', views.DeleteTaskViewByName.as_view())
    ,path('delete-task-job-by-uuid', views.DeleteTaskViewByUUID.as_view())
    #,path('get-task', views.GetTask.as_view())
]

urlpatterns += [
    path('api-auth', include('rest_framework.urls'))
]
