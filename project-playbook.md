# TOC

1. [Virtual Environment](#virtualenv)
1. [Installing Django](#installing-django)
1. [Start Django Project](#start-django-project)
1. [Start Django App](#start-django-app)
1. [Running a development server](#runserver)
1. [](#)
1. [](#)
1. [](#)
1. [](#)

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

<h1 id="add-models">Add a Task Model</h1>

We start by adding a model which will be a basis for our database structure.

In models.py:

    from django.db import models
    
    
    class Task(models.Model):
        content = models.TextField()
        completed = models.BooleanField(default=False) 
        
        
Here we define a model called `Task` with two fields:
- `content` is the content of the todo. Therefore we define it as a `models.TextField()`. 

- `completed` denotes whether the `Task` has been completed or not. For this we use a `modela.BooleanField()` and specifiy that new entries should have this field marked as `False` (we do not create task that are born completed).

<h1 id="migrations">Migrations</h1>

Now we have to create migrations for our app so django knows how to build the database.

    (venv) $ ./manage.py makemigrations
    Migrations for 'todo':
      todo/migrations/0001_initial.py:
        - Create model Task
       
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
    
    @admin.register(models.Task)
    class TaskAdmin(admin.ModelAdmin):
        pass


<h1 id="create-an-admin-user">Create an Admin User</h1>

    (venv) $ ./manage.py createsuperuser
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

<h1 id="create-a-task">Create a Task</h1>

Now you can create a Task. 

Tasks will be represented as "Task object". We can fix that by overriding the `__str__` method of the model:

    class Task(models.Model):
        content = models.TextField()
        completed = models.BooleanField(default=False)
        
        def __str__(self):
            return self.content
            

<h1 id="shining-up-the-admin">Shining up the admin</h1>

We can do some nifty things with the admin. Add `list_display` to the admin to show more columns:

    @admin.register(models.Task)
    class TaskAdmin(admin.ModelAdmin):
        list_display = ['content', 'completed']
        
Now we can see if an Task has been completed or not.

<h1 id="creating-your-own-interface">Creating your own interface</h1>

The admin is good for admin work and checking if your model actually makes sense. But we don't want our users to use the admin. We should make something ourselves for this.

For that we need three things:

- A view
- A template
- An URL conf


<h1 id="writing-a-view">Writing a view</h1>

We need to have some code which fetches data from the database and renders a template with the data.

We already have a file called `todo/views.py`, this is where we will write the views for our application.

We start by writing a "function based view". Django also supports "class based views", but for learning purposes we will only work with "function based views".

`todo/views.py` should look like:

    from django.shortcuts import render
    from . import models


    def task_list(request, **kwargs):
        tasks = models.Task.objects.all()
        context = {'tasks': tasks}
        return render(request, 'task_list.html', context)
        
        
- `tasks = models.Task.objects.all()` is where we query our database for all `Task` entries. This returns a `QuerySet`.
- `context = {'tasks': tasks}`; here we create our context which will be used to render the template with.
- At last we `return render(request, 'task_list.html', context)` which means that we return a response in the request-response cycle with the `task_list.html` template rendered using the `context` context.

<h1 id="writing-a-template">Writing a template</h1>

The view refers to a template, lets write it!

We should have a place to store our templates. Django searches for templates in `<app-name>/templates/` by default.

So we create a `todo/templates/` directory. In this we want only one template. Lets call it `todo/templates/task_list.html`.

The template should look like this:

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Todo</title>
    </head>
    <body>

    <ul>
    {% for task in tasks %}
      <li>
        {{ task.content }} -
        {% if task.completed %}
          Done!
        {% else %}
          <a href="">Mark as done</a>
        {% endif %}
      </li>
    {% endfor %}
    </ul>

    </body>
    </html>


Django has a template language which is quite straight forward:

- `{% for task in tasks %}` tells the template engine to iterate through the `tasks` query we made in the view. A `{% for ... %}` always ends with a `{% endfor %}`
- `{% if task.completed %}` makes a check for the boolean value of the give variable, in this case `taske.completed`. In this specific code it means that if `task.completed` is `True` we will show "Done!", otherwise we'll show a link to something that marks the given task as completed. A `{% if ... %}` always ends with a `{% endif %}`.
- `{{ task.content }}` means that we want to access the `content` attribute of the `task` object.

<h1 id="hooking-up-urls">Hooking up URLs</h1>

Every time a request comes in, the URL requested will be used to figure out which view to use. This mapping we call an URL Conf. The main URL conf is placed in `todo_project/urls.py`.

    from django.conf.urls import url
    from django.contrib import admin

    from todo import views
        url(r'^$', views.todo_list, name='todo_list'),
        url(r'^admin/', admin.site.urls),
    ]
    
    
<h1 id="creating-a-task">Creating a task</h1>

To create a task we have to make some additions to our code:


Update `todo/templates/task_list.html` like this (in the \<body\> tags):

    <form method="POST">
      {% csrf_token %}
      <input type="text" name="content" />
      <button type="submit">Add</button>
    </form>

    <hr />

    <ul>
    {% for task in tasks %}
      <li>
        {{ task.content }} -
        {% if task.completed %}
          Done!
        {% else %}
          <a href="">Mark as done</a>
        {% endif %}
      </li>
    {% endfor %}
    </ul>


Update `views.py` like this:

    def task_list(request, **kwargs):
        if request.method == "POST":
            task_content = request.POST['content']
            new_task = models.Task(content=task_content)
            new_task.save()
            return redirect('task-list')

        tasks = models.Task.objects.all()
        context = {'tasks': tasks}
        return render(request, 'task_list.html', context)


<h1 id="">Marking a task as fixed</h1>

To mark a task as fixed we write a very simple view:


    def task_complete(request, **kwargs):
        pk = kwargs.get('pk')
        task = models.Task.objects.get(pk=pk)
        task.completed = True
        task.save()
        return redirect('task-list')
        
        
And then we add this view to the URL conf:


    urlpatterns = [
        url(r'^$', views.task_list, name='task-list'),
        url(r'^(?P<pk>\d+)/$', views.task_complete, name='task-complete'),
        url(r'^admin/', admin.site.urls),
    ]
    
And last we update the template to use this new URL when pressing the completion-link:

    <form method="POST">
      {% csrf_token %}
      <input type="text" name="content" />
      <button type="submit">Add</button>
    </form>

    <hr />

    <ul>
    {% for task in tasks %}
      <li>
        {{ task.content }} -
        {% if task.completed %}
          Done!
        {% else %}
          <a href="{% url 'task-complete' pk=task.pk %}">Mark as done</a>
        {% endif %}
      </li>
    {% endfor %}
    </ul>
    

Here we are using the `{% url ... %}` template tag, which uses the names from the URLs to figure out what to link to.

<h1 id="further-tasks">Further tasks</h1>

- Separate completed and non-completed tasks (hint: use the QuerySet `.filter()` method)
- Make it possible to delete tasks
- Make it possible to mark already completed tasks as not completed.
- Make it possible to update the content of tasks
- Use Django forms
