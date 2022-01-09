from django.contrib import admin
from djSheduler.models import task
from djSheduler.models import task_log
from djSheduler.models import task_operation
from djSheduler.models import task_operation_log


admin.site.register(task)
admin.site.register(task_log)
admin.site.register(task_operation)
admin.site.register(task_operation_log)
