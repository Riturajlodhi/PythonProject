# Django is specially for database driven websites.
# Django follows MVT design pattern (Model view template).

# Django create app - python manage.py starapp members
# Django views
# are the python functions that take http requests and return http response like html pages

from django.shortcuts import render

print(print("""
# Django from scratch

Writing first django app p-1 --
firstly install django - if installed check thek version by typing in terminal python -m djnsgo --version

Creating a project - cd to change the location wherever you want to keep the project
 run this in terminal --> django-admin startproject meraproject meraprojectfolder
 this will create a directory with a project name called meraproject inside it like 
 
 meraprojectfolder/
       manage.py
    meraproject
             __init__.py
             settings.py
             urls.py
             asgi.py
             wsgi.py
    
Getting runtime help --

run django-admin help , django-admin help --commands , django-admin help <command>

Displaying debug output -- use --verbosity after django-admin
******dbt****
Available Commands:-
check  :-
django-admin check auth admin my_app , 

>> --tags TAGS,-t TAGS django-admin
>> --database DATABASE
>> django-admin check --database default --database other

Manage.py is a command-line tool that controls your Django project
1). Run server -- python manage.py runserver starts django website
2). Create app -- python manage.py startapp blog
creates folder -- models.py, views.py, admin.py
3). Database Migrations (v.imp) -- step 1} create migration - python manage.py makemigrations
converts models -> migration file
step 2} apply migration - python manage.py migrate
Create tables in database 
Model change = migrate again

4). Create Admin User --
python manage.py createsuperuser - It asks username,email,password
then login at :- /admin

5). Django shell (Power tool) -->
python manage.py shell - used for :- testing models, debugging orm

Example :- fromblog.models import Blog
           Blog.objects.all()
6). Collect static (deployment)

python manage.py collectstatic

Used when deploying:- css,js,images
Django Admin - built in dashboard to manage your database visually on browser itself add,edit,delete data instead of writing sql

Step by Step django admin
1). enable admin(already enabled by default) in settings.py file :-

INSTALLED_APPS = [
   'django.contrib.admin',
]

2). create superuser -->
python manage.py createsuperuser
login:-
http://127.0.0.1:8000/admin

3).Register Model in Admin
# models.py
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

Register it:-
# admin.py
from django.contrib import admin
from .models import Blog

admin.site.register(Blog)

Add data from Admin - login to admin > click blog > add record > save

> List display (Show columns)

class BlogAdmin(admin.ModelAdmin)
    list_display = ('title','id')

admin.site.register(Blog, BlogAdmin)

> Search Bar

search_fields = ('title',)

> Filters

list_filter = ('id',)

> Read-only Fields

readonly_fields = ('id',) -- used for :- timestamps, auto fields

myapp/: a directory that is actual python package for your project
Its name is python package name you ll need to use to import anything inside it(myapp.urls)

__init__.py :- An empty file that tells python that this directory should be considered a python package)

settings.py :- settings/configuration for this django project. Django settings will tell you how settings work

urls.py :- URL declarations for this django project, a "table of contents" of your Django-powered site. 
      
1). Creating a Project :-
      django-admin startproject mysite djangotutorial
      
2).The development server
     python manage.py runserver
3).Creating the polls app
     python manage.py startapp polls
     
4).Write your first view
polls/views.py
    from django.http import HttpResponse
    
    def index(request):
         return HttpResponse("Hello, world. You're at the polls index.")

5).writing your first view
polls/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
     
6). Database setup
by default in settings.py INSTALLED_APPS contains the following apps  
django.contrib.admin - the admin site
django.contrib.auth - authentication system
django.contrib.contenttypes - framework for content types
django.contrib.sessions - a session framework
            .messages - messaging framework
            .staticfiles - framework for managing static files)

python manage.py migrate
            
Creating models------
            
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
            
======Activating models--
            "create polls.apps.PollsConfig" in installed apps in settings.py
            
            we have included app in the project
            
$ python manage.py makemigrations polls
            by telling this you are telling Django that you have some changes to your models
   
$ python manage.py sqlmigrate polls 0001

$ python manage.py migrate

==++++== Playing with the API -----
         
 to invoke the python shell, 
    $ python manage.py shell
     
-----> Model field reference <-----
       Field options -- null
       Field.null -- empty values as NULL in the database
       
       Avoid using null on string-based fields such as Charfield and TextField
       2). blank ---> Field.blank If true then field is allowed to be blank false is default
       3). choices ---> Field.choices[source]
       
-----> Making queries
Basic Queries -- get all records -- Question.objects.all()
-- returns all questions

-- Get Single Object -- Question.objects.get(id=1)
If object doesnt exist --> error
safer way :- Question.objects.filter(id=1)

---> Filter Data 
Question.objects.filter(question_text="What's up?")

Question.objects.filter(id__gt=2)
lookups - __gt, __lt, __contains, __startswith, __in

Question.objects.filter(id__in=[1,2,3])

3).= Query Related Objects(Foreign Key)

Get choices of a question -- 

q = Question.objects.get(id=1)
q.choice_set.all()
            
Reverse Query 

--> Choice.objects.filter(question__id=1)
(or)
--> Choice.objects..filter(question__question_text__contains="Python")

4). Create data using ORM
Question.objects.create(
    question_text="Favorite 
)

--> After creating data models - how to use API