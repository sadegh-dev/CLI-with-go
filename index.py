"""
Python *5
OOP    *5
Design Patterns *3
RabbitMQ  *3

Django *5
DRF    *5
Celery *5

PostgreSQL *3
MongoDB    *3

Linux  *3
Docker *3
GIT    *5
GitLab CI/CD  *3

Html / CSS  *5
Bootstrap   *3


############### [PYTHON] ###############

# install
# pip
# env
# general
# input
# print
# comment
# anaconda
# file

# algorithms
# clean_code
# pep8

# variable
# math
# string
# rando_module
# math_module

# iteration
# array
# list
# set
# tuple
# dictionary

# collections_module
# itertools_module
# numpy_module

# comprehension
# generators

# decorator
# lambda
# functions
# functools_module
# module

# context_manager
# annotations
# regex
# security

# Multi_Threading
# Multi_Processing
# ASYNCIO I/O

# web Scraping
	- ...

# RabbitMQ
	- ...

# OOP
	- list class methods
	- points of OOP
	- obj.__dict__
	- class/instance variable
	- comparison Methods
	- Container object
	- iterable object
	- method chaning
	+ attributes management
		- delattr
		- getattr
		- hasattr
		- setattr
	- polymorphism
	- object input another object
	- abstract class - abstract methods
	+ classes inheritance
		- super()
	- mixin class
	- inheritancec from built-in objects
	- multi inheritance
	- access levels in class
	- decorator property
	+ methods types in class
		- instance method
		- static method
		- class method
	+ magic-special methods [built-in] in class
		- [Not USE] __del__
		- __init__
		- __new__
		- __str__
		- __repr__
		- __call__
		- __add__
		- __len__
		- __missing__

		- __getitem__
		- __setitem__
		- __delitem__

		- __getattr__
		- __setattr__
		- __delattr__
		- __getattribute__

		- __reversed__
		- __bool__

	- Meta class
	- nasted class
	+ descriptors
		- @property [getter]
		- @name.setter
		- @name.deleter
	+ descriptors
		- __set_name__
		- __get__
		- __set__
		- __delete__

	- SOLID architecture



# design patterns
	- singleton [creational]
	- factory [creational]
	- abstract factory [creational]
	- prototype [creational]
	- builder [creational]
	- adapter [structural]
	- decorator [structural]
	- facade [structural]
	- proxy [structural]
	- chain of responsibility [behavioral]
	- strategy [behavioral]
	- iterator [behavioral]
	- observer [behavioral]
	- template methods [behavioral]
	- state [behavioral]
	- composite [creational]



# Unit_Test
	- general
	- doctest module
	- unittest module
	- nose module
	- pytest module
	- selenium module


# Debugging
	- general debugging
	- errors management
	- EAFP
	- error types
	- more except
	- EOF error
	- EOL error
	- error message
	- custom except
	- custom except class
	- debugging in VScode
	- errors logfile
	- circular imports / circular dependency


# Benchmarking
	- timeit module
	- line_profile module
	- memory_profile module
	- resource module


[PYTHON MODULES]

# python_docx_module
# datetime_module
# requests_module
# beautifulsoup_module
# platform_module
# sys_module
# os_module
# json_module
# time_module
# operator_module
# whois_domain
# dataclass_module
# contextlib_module
# logging_module
# smtplib_module
# pillow_module
# pylint_module
# mypy_module
# pickle_module
# queue_module



############## [DJANGO] ###############

# launch
	- config settings for launch
	- delete static settings from main urls.py
	- upload django project on server


# general
	- general points
	- request.method
	- running multiple Django projects through different ports 
	- run command on shell
	- Meta class


# install
	- create project
	- rename project


# settings
	- general config
	- general variables
	- connect to email-service [like gmail]


# HttpRequest


# templates
	- default template structure
	- center template structure
	- template structure connect react
	- send data from views to template
	- access to HTTP-method
	- initialize the variable by with
	- create link
	- partitioning HTML files
	- pagination
	- list tags
	- built-in template filter
	- create html page 404


# static/media
	- static files
	- media files
	- media and statc files structures
	- run collectstatic command
	- use jquery


# views
	- points of views
	- decoratores
	- structure views function
	- direct use HTML-tag in function-views
	- redirect in views
	+ CBV : class base view [https://ccbv.co.uk/]
		- View class
		- TemplateView class
		- RedirectView class
		- ListView class
		- DetailView class
		- MonthArchiveView class

		- FormView class
		- CreateView class
		- DeleteView class
		- UpdateView class

		- mixin
		- FormMixin

	- manager types [like: get, all, filter]
	- custom decorator for computing querySet time
	- optimization QuerySet for get data in relation-class
	- list field-lookups of querySet
	- F-experssions
	- union several querySet
	- create-update-delete-add
	- create search
	- complex lookup – Q function
	- Full text search
	- create custom manager
	- Http 404


# messages
	- points of message
	- create message


# signals
	- points of signals
	- practical examples of signals
	- basic signal settings
	- pre_save - post_save
	- way of call the signals method
	- pre_delete - post_delete


# urls
	- points of urls
	- Error handling
	- create url by parameters
	- Initial value for passed arguments
	- path function
	- re_path function
	- set url-name
	- cancellation of famous url-name
	- set namespace for app
	- create unique url-slug
	- send parameters by url to views
	- persian url
	- set slug in admin panel
	- reverse, reverse_lazy methods
	- difference in methods of reverse - reverse_lazy
	- grouping urlpatterns
	- Subset creation for addresses with a common pattern


# admin
	- points of admin
	- default admin-panel
	- custom admin-panel for the class
	- admin action
	- admin title
	- custom style admin-panel
	- creating computational field in admin-panel
	- set validation-field in admin-panel


# app
	- points of app
	- create new app
	- create app inside main directory


# models
	- points of models
	- create package model
	- ORM : object relational mapping
	- naming model
	- field types
	- field options
	+ related methods
		- create method
		- save method
		- delete method
		- add method
		- remove method
		- clear method
		- set method
		- update method
	+ overrite default methods
		- override save method
		- override delete method
	- creating proccessing functions on field
	- __str__ method in model-class
	- get_absolute_url method in model-class
	- Meta class in model-class
	+ abstract - inheritance
		- abstract base classes
		- multi-table inheritance
		- proxy models
	+ relation between classes
		- one to many [ForeignKey]
		- one to one
		- many to many
		- intermediate model
		- backward relation
		- on_delete attribute
		- limit_choices_to attribute
	- migrations
	- content types


# middleware


# db
	- points of database
	- sqlite3
	- postgreSQL
	- mySQL
	- mongoDB
	- use several databases


# forms
	- strategy
	- points of forms
	- normal form structure
	- list of field-form
	- list of widgets
	- create date-time field
	- create shamsi date-time field
	- create form by forms.ModelForm
	- help_desk – widget – error_messages in forms.ModelForm
	- create edit-form by forms.ModelForm
	- edit 2 model-class by 1 form
	- create delete-button by forms.ModelForm
	- initialization fields-form
	- set reCAPTCHA in form
	- create form by forms.Form
	- create 2 form in 1 page
	- different ways of displayeing form in html-page
	- default validation and form errors
	- create custom validation form
	- set persian form-errors
	- deactive validation-fom [not recommended]
	- management forms.ValidationError


# Authentication
	- points of auth
	-[NOT USE] use default User-model-class
	-[NOT USE] relation one-to-one with default User-model-class
	-* custom User-model-class
	- different AbstractUser and AbstractBaseUser
	- use CBV in authentication Views
	- change authentication password
	- oauth
	- reset password by CBV
	- signup new-user by create_user method in default User-model-class
	- default login method
	-[NOT USE] use authentication-backend for get Email and use comparison username and email
	- default logout method
	- access user-data in views after login
	- access user-data in template-file after login
	- block out run function-views for user not logged
	- block out run class-views for user not logged
	-[NOT USE] default register method [with more fields]
	-[NOT USE] create one-to-one User-class with profile-class
	-[NOT USE]	create password and confirm password fields
	- determining the user path after logout
	- allow access to own page, not others
	- login by phone number


# security
	- security topics
	- protected admin-panel-url
	- security of period upload project
	- cross site scripting (XSS)
	- python-decouple
	- points of security


# permission

# debugging


# celery
	- points of celery
	- use celery in python code
	- flower
	- management comman-line utilities
	- signatures in celery
	- use celery in django project
	- example of django-celery project
	- celery beat
	- example2 of dajngo-celery project
	- worker running in background by supervisor



# caching
	- plan
	- cache levels
	- caching by redis
	- caching by memcached
	- cache arguments
	- cache full webiste page
	- cache views
	- cache template
	- delete old cache when new data is added
	- The low-level cache API
	- downstream caches


# sessions


# testing
	- points of testing
	- testing plan
	- testing directory
	- run tests
	- test inheritance
	- assertions
	- testing tools
	- testing urls
	- testing forms
	- testing models
	- testing views
	+ pytest module for django project
		- pytest marks functions
		- custom mark functions
		- fixture method


# aggregation


# annotate
	- aggregating annotations



# gunicorn

# dockerize



# modules
	- custom module
	- Markdown module
	- RegEx module
	- ckeditor module
	- pillow module
	- timezone module
	- sorl-thumbnail module
	- django-filter module




########### [DRF] ##################


# drf plan
# postman
# json
# use foreign API
# start create API
# install drf
# response
# request


# serializer
	- points of serializer
	- create serializer
	- create serializer by ModelSerializer
	- definition extra fields in serializer
	- some properties of Serializer-fields
	-[NOT USE] BaseSerializer
	- serializer inheritance
	+ serializer relations
		- StringRelatedField
		- PrimaryKeyRelatedField
		- HyperlinkedRelatedField
	+ validation in serializer
		- Field-level
		- object-level
		- validators


# views
	+ class base View
		- ViewSet
		- generics
		- APIView
	- function View


# viewset
	- points of viewset
	- ModelViewSet
	- ReadOnlyModelViewSet


# class-field types and API-data
# send json-data and create record-data
# send json-data and update record-data
# send json-data and delete record-data
# two behavioral of save-method
# status codes


# authentication
	- BasicAuthentication
	- TokenAuthentication
		- ways of create Token
		- login with Token
	- SessionAuthentication
	- JWT


# permissions
	- point of premissions
	- set permissions of function or class in Views
	- types of permissions


# throttling
# caching


# routers
	- points of routers
	- SimpleRouter
	- DefaultRouter


# Renderers
# pagination
# practical example and its tips
# testing
# swagger




########### [LINUX] ################


# topics of linux
# directory structure
# work with terminal
# curl commands
# environment variables
# packeage manager
# process management
# desktop environment



########### [DEVOPS] ###############

# server

# gitlab-ci-cd

# git

# docker

# azeru

# nginx










##################################################3
####################################################
###################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
@@@@@@@@@@@@@@@@@@@@22
django channels
asyncio
mypy
type annotations
modular design
Event-driven architectur
ways of authentication & authorization
unit testing
TDD : test-driven development
automated testing
python libraries
OOP : SOLID / KISS / DRY
Design patterns
error handling

RDBMS
database design
query optimization

multi threading
multi proccesing

data engineering
server config
visual studio code
-----------------------
monitoring service
postman
agile / scrum
code review


http protochol
CI / CD
gitlab CI/CD
[ postgresql, elasticsearch, redis, mongo, MinIO, ClickHouse, Influx, Prometheus, ]
[داشبورد: grafana, kibana, metabase, amplitude.]
ll
-----------------------

Redis
webSocket programming
mongodb

soap
nginx



"""
