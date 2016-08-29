# TOC

1. [Virtual Environment](#virtualenv)
1. [Installing Django](#installing-django)
1. [Start Django Project](#start-django-project)
1. [Start Django App](#start-django-app)

<h1 id="virtualenv">Virtual Environment</h1>

Virtual environment enables us to run different versions of dependencies. This is useful if you have multiple projects that depend on different versions of third party applications.

    $ virtualenv venv  # Create the environment
    $ source venv/bin/activate # 
    (venv) $ python -c 'import sys; print(sys.executable)'
    # The python binary will be in the virtual environment
    
    
<h1 id="installing-django">Installing Django</h1>

    (venv) $ pip install django


<h1 id="start-django-project">Start a Django Project</h1>

    (venv) $ django-admin startproject todo_project
    (venv) $ cd todo_project/
    (venv) $ tree
    .
    ├── manage.py
    └── todo_project
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

    1 directory, 5 files
    
    
<h1 id="runserver">Running the Development Server</h1>

You can now run the development server in the project

    (venv) $ ./manage.py runserver
    Performing system checks...

    System check identified no issues (0 silenced).
    August 24, 2016 - 20:36:34
    Django version 1.10, using settings 'todo_project.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    
Then visit http://127.0.0.1:8000/ - It worked!
    
 
<h1 id="start-django-app">Start a Django App</h1>

We need some content!

    (venv) $ ./manage.py startapp todo
    (venv) $ tree
    .
    ├── manage.py
    ├── todo
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── todo_project
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
        
To tell Django that this new app is to be used we have to add it to the `INSTALLED_APPS` variable in `settings.py`:

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'todo',
    ]

<h1 id="add-models">Add a TodoItem Model</h1>

We start by adding a model which will be a basis for our database structure.

In models.py:

    from django.db import models
    
    
    class TodoItem(models.Model):
        content = models.TextField()
        completed = models.BooleanField(default=False) 

<h1 id="migrations">Migrations</h1>

Now we have to create migrations for our app so django knows how to build the database.

    (venv) $ ./manage.py makemigrations
    Migrations for 'todo':
      todo/migrations/0001_initial.py:
        - Create model TodoItem
       
Then apply the actual migration:
    
    (venv) $ ./manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, sessions, todo
    Running migrations:
      Rendering model states... DONE
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying sessions.0001_initial... OK
      Applying todo.0001_initial... OK
      
<h1 id="the-admin">The admin</h1>

We can easily activate the admin editing `todo/admin.py` with the following content:

    from django.contrib import admin
    
    from . import models
    
    @admin.register(models.TodoItem)
    class TodoItemAdmin(admin.ModelAdmin):
        pass


<h1 id="create-an-admin-user">Create an Admin User</h1>

    (venv) $ ./manage.py createuser
    ./manage.py createsuperuser
    Username (leave blank to use 'valberg'):
    Email address:
    Password:
    Superuser created successfully.
    
Beware of the password constraints!


<h1 id="login-into-the-admin">Login into the Admin</h1>

As before start the development server like this:

    (venv) $ ./manage.py runserver
    Performing system checks...

    System check identified no issues (0 silenced).
    August 24, 2016 - 20:36:34
    Django version 1.10, using settings 'todo_project.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    
Now go to http://127.0.0.1:8000/admin/

<h1 id=""></h1>
<h1 id=""></h1>
<h1 id=""></h1>
<h1 id=""></h1>
<h1 id=""></h1>
<h1 id=""></h1>
<h1 id=""></h1>
<h1 id=""></h1>
<h1 id=""></h1>
<h1 id=""></h1>
<h1 id=""></h1>
<h1 id=""></h1>
<h1 id=""></h1>
<h1 id=""></h1>
<h1 id=""></h1>
