##########
User guide
##########


Installing backend
==================

Linux
_____

Start zero (optional)
---------------------

Create project folder (optional)::

    $ mkdir demoTaskBrocker
    $ cd demoTaskBrocker

Create virtual environment in new fouldel (optional)::

    $ python3 -m venv venv

Activate virtual environment (optional)::

    $ source venv/bin/activate

Install django::

    $ pip install django

Start new django project::

    $ django-admin startproject core .

Deploy
------
 
Clone repository::

    $ git clone https://github.com/NeoUKR/djTaskBrocker.git

Install dependancy::

    $ cd djTaskBrocker
    $ pip install -r requirements.txt
    $ cd ..


Connect to Django project
-------------------------

Update `settings.py`::
    
    INSTALLED_APPS = [
        'djTaskBrocker',
        'rest_framework',
    ]


Update `urls.py`::

    from django.urls import include

    urlpatterns = [
        path('tb/', include('djTaskBrocker.urls')),
    ]

Update DB structures::

    $ python3 manage.py makemigrations djTaskBrocker
    $ python3 manage.py migrate

Now you can run project::

    $ python3 manage runserver

Wen all is well you should see string::

    $ ############runing sheduler##############

Task example
____________

Append demo operations to task list::

    $ cd djTaskBrocker
    $ cd demo
    $ python3 demoOperation.py addDemo1

Check on call API `<http://127.0.0.1:8000/tb/api/get-list>` you shoud see new task::

    [
        {
            "uuid": "3df2e91a-d9db-11ec-be98-9198762a5cd1",
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
            "task_module_name": "demo.demoSingleReglament",
            "task_function_name": "Print",
            "execute": false
        }
    ]

Start task::

    $ python3 demoOperation.py startDemo1

When all is well you see periodical call function in console::

    %%Start 'SHEDULE_APP' moment: 2022-05-22 14:31:31.373335
    ID: 3df2e91a-d9db-11ec-be98-9198762a5cd1
    App name: djTaskBrocker
    Module name: demo.demoSingleReglament
    Function name: Print
    Atribute: Print
    execute task at 2022-05-22 14:31:31.373431

Stop task::

    $ python3 demoOperation.py stopDemo1

Delete task::

    $ python3 demoOperation.py delDemo1

Installing frontend
===================

Linux
_____

Deploy
------

Clone repository to exist django project::

    $ git clone https://github.com/NeoUKR/djTaskBrockerFrontendAdmin.git

Initialization
--------------

Install dependancy::

    $ cd djTaskBrockerFrontendAdmin
    $ npm install

Compile project::

    $ npm run dev

Connect to Django project
-------------------------

Update `settings.py`::
    
    INSTALLED_APPS = [
        'djTaskBrockerFrontendAdmin',
    ]

Update `urls.py`::

    from django.urls import include

    urlpatterns = [
        path('tb/dashboard/', include('djTaskBrockerFrontendAdmin.urls')),
    ]

Now you can run project and connect to dashboard::

    $ http://127.0.0.1:8000/tb/dashboard



Connect to Django project
-------------------------

Connect

Initialization
--------------

Initialization


Operations with task
====================

test :doc:`apirest`

"...writing...further will be...."