########
API REST
########


get-list
========

Отримуємо список завдань

    GET /tb/api/get-list

**Parameters**:

None

**Example response**:

.. sourcecode:: json
[
    {
        "uuid": "361d0ef4-c663-11ec-a81c-a9552d28665d",
        "id_name": "printData1",
        "name": "printind data",
        "type": "single",
        "max_instances": 1,
        "trigger_type": "interval",
        "trigger_interval_weeks": null,
        "trigger_interval_days": null,
        "trigger_interval_hours": null,
        "trigger_interval_minutes": null,
        "trigger_interval_seconds": 5.0,
        "task_app_name": "djTaskBrocker",
        "task_module_name": "testSingleReglament",
        "task_function_name": "Print",
        "execute": false
    },
    {
        "uuid": "e9cecc7e-c818-11ec-89d1-b98329cca7c2",
        "id_name": "demo_interval",
        "name": "Demo interval",
        "type": "single",
        "max_instances": 1,
        "trigger_type": "interval",
        "trigger_interval_weeks": null,
        "trigger_interval_days": null,
        "trigger_interval_hours": null,
        "trigger_interval_minutes": null,
        "trigger_interval_seconds": 5.0,
        "task_app_name": "djTaskBrocker",
        "task_module_name": "testSingleReglament",
        "task_function_name": "Print",
        "execute": false
    }
]:

stop-job-by-name
================

    POST /tb/api/stop-job-by-name

**Parameters**:

'id_name': String 
(internal Task name)


**Example response**:


Reporting bugs
==============

.. include:: ../README.rst
   :start-after: Reporting bugs
                 --------------
