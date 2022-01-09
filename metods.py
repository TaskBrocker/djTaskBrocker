def appendOperation(idNameTask, inParameters):
    from djSheduler.models import task
    from djSheduler.models import task_operation
    
    multyTask = task.objects.filter(id_name = idNameTask).first()
    
    if multyTask != None:
        newOperation = task_operation()
        newOperation.task_id = multyTask.id
        newOperation.parameters = inParameters;
        newOperation.save() 