import sys
from django.apps import AppConfig
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def schedule_api(*args):
    from django.db.models.functions import Now
    from time import sleep
    from djSheduler.models import task_log    
    import importlib
    
    print("%%Start 'SHEDULE_APP' moment: " + str(datetime.utcnow().now()))
    print("ID: " + args[0]);
    print("App name: " + args[1]);
    print("Module name: " + args[2]);
    print("Function name: " + args[3]);
    print("Atribute: ", end = "");
    print(args[3])
    
    newTask = task_log(task_id=args[0], moment_start=Now())
    newTask.save();
    
    operations = importlib.import_module(args[1] + '.' + args[2])
    
    result = getattr(operations, args[3])(args[4])
     
    #result = operations.test_operation(args[1]);
    
    if type(result) == 'dict':
        if "status" in result:
            if "status" in result:
                newTask.result_status = result["status"]
        if "message" in result:
            if "message" in result:       
                newTask.message = result["message"]
    
    newTask.moment_end = Now();
    newTask.save();
    
def multitask_schedule(*args):
    print("#1: Start task operation")#Debug
    from django.db.models.functions import Now
    from djSheduler.models import task_operation
    from djSheduler.models import task_operation_log    
    import importlib
    
    print("#2: Get operations")#Debug
    #print("#1Start operation")#Debug
    firstOperation = task_operation.objects.all().filter(executing = False, finished = False).first();
    
    if firstOperation != None:
        
        start_moment = Now(); 
        
        firstOperation.executing = True;
        firstOperation.moment_start = start_moment;
        firstOperation.moment_end = None;
        firstOperation.result_status = None;
        firstOperation.result_status_internal = None
        firstOperation.message = None
        firstOperation.message_internal = None

        
        firstOperation.save();
        #print(firstOperation);

        newOperationLog = task_operation_log(task_operation_id=args[0], moment_start=Now())
        newOperationLog.moment_start = start_moment;
        newOperationLog.save();
    
        result_operation = {"status": 200, "message": ""} 
        result={"status":0, "message":""}
        
        try:
            print("#4: Start operation")#Debug
            print("#4.1: Module library name: ", end="")
            print(args[1])
            
            operations = importlib.import_module(args[1] + '.' + args[2])
            #operations = importlib.import_module(args[1] + '.' + args[2])
            
            #resultOperation = getattr(operations, "test_multioperation")(3,4)
            result = getattr(operations, args[3])(args[4], firstOperation.parameters)
            
            if type(result) == 'dict':
                if not "status" in result:
                    result["status"] = 0;
                if "message" in result:
                    result["message"] = "";
                    
                if result["status"] != 0:
                    result_operation["status"] = 207
                    result_operation["message"] = "Multistatus"
                    
            else:
                result={"status":0, "message":""}
                result_operation["status"] = 230
                result_operation["message"] = "No return status from operation"
            
        except Exception as e:
            result_operation["status"] = 500
            result_operation["message"] = "Executing exception: " + str(e)
        
        print("#5: wrire logs")#Debug
        end_moment = Now()
        print('End moment: ' + str(end_moment)) 
            
        newOperationLog.parameters = firstOperation.parameters;
        newOperationLog.result_status = result_operation["status"]
        newOperationLog.result_status_internal = result["status"]
        newOperationLog.message = result_operation["message"]
        newOperationLog.message_internal = result["message"]
        
        newOperationLog.moment_end = end_moment;
        newOperationLog.save();
        
        firstOperation.executing = False;
        firstOperation.finished = True;
        
        firstOperation.result_status = result_operation["status"]
        firstOperation.result_status_internal = result["status"]
        firstOperation.message = result_operation["message"]
        firstOperation.message_internal = result["message"]
        
        firstOperation.moment_end = end_moment;
        firstOperation.save();
        
        print("#5: End operation")#Debug
    
    
class djShedulerConfig(AppConfig):
    name = 'djSheduler';
    test = 'ok ok';
    scheduler = None;

    def ready(self):
        #print("start server")
        
        if 'runserver' in sys.argv:
            #print("runing parser")
            
            self.scheduler = BackgroundScheduler()
            
            #try:
            from djSheduler.models import task
            
            fetchAll = task.objects.all().filter(execute = True);
            
            print("#Step 3: " + str(len(fetchAll)))
            print(fetchAll)
            
            for elTask in fetchAll:
                
                print('id: ' + str(elTask.id))
                print('Name: ' + str(elTask.name)) 
                print('Type: ' + str(elTask.type))
                print('Trigger_type: ' + str(elTask.trigger_type))
                print('App name: ' + str(elTask.task_app_name))
                print('Module name: ' + str(elTask.task_module_name))
                print('Function name: ' + str(elTask.task_function_name))
                print('Execute: ' + str(elTask.execute))
                
                
                triggerType = str(elTask.trigger_type);
                #print("Trigger type:" + triggerType)
                
                taskARG = ();
                taskARG = taskARG + (str(elTask.id),); 
                taskARG = taskARG + (str(elTask.task_app_name),)
                taskARG = taskARG + (str(elTask.task_module_name),)
                taskARG = taskARG + (str(elTask.task_function_name),)
                taskARG = taskARG + (45,)
                
                parameters = {};
                
                for elTaskField in elTask._meta.get_fields():
                    fieldName = elTaskField.name;
                    #print("Len trigge type: " + str(len(triggerType)))
                    #print("Row name: [" + fieldName + "] ", end = '');
                    triggerTypeRow = fieldName[8:(8+len(triggerType))]
                    #print("Trigger Type ROW: {" + triggerTypeRow + "}");
                     
                    if  triggerTypeRow == triggerType:
                        triggerParameterName = fieldName[(8 + len(triggerType) + 1):]
                        #print("Parameter Name: " + triggerParameterName);
                        fieldValue = getattr(elTask, fieldName)
                        if fieldValue != None:
                            parameters[triggerParameterName] = getattr(elTask, fieldName); 
                
                print("all parameters:")#Debug
                print(parameters)                   
                
                print("Sheduling job")#Debug    
                
                if elTask.type == 'multy':
                    self.scheduler.add_job(multitask_schedule, str(elTask.trigger_type), **parameters, id=str(elTask.id), args = taskARG, max_instances = 5)
                else:
                    self.scheduler.add_job(schedule_api, str(elTask.trigger_type), **parameters, id=str(elTask.id), args = taskARG)
            
                self.scheduler.start()        
        
        #print("ok 1 " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'));#Debug
        
        
        '''
        from reglament.models import task
        from time import sleep
        import rpyc
        
        fetchAll = task.objects.all();
        
        for elTask in fetchAll:
            print('Name: ' + elTask.name) 
            print('UUID: ' + elTask.uuid)
            print('Module name: ' + elTask.module_name)
        
        
        print("ok 1 " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'));
        conn = rpyc.connect('localhost', 12345)
        job = conn.root.add_job('server:print_text', 'interval', args=['Hello, World'], seconds=2)
        sleep(10)
        conn.root.remove_job(job.id)        
        print("ok 2 " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'));
        '''
