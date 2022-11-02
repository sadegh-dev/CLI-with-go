"""
[PYTHON]

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

# comprehension
# generators

# collections_module
# itertools_module
# numpy_module


# decorator
# lambda
# functions
# functools_module
# module


# context_manager
# annotations
# regex
# security
# multi_threading


# scraping
	- ...


# rabbitMQ
	- ...


# OOP

	- list class Methods
	- obj.__dict__
	- class variables
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
	- object (object)
	- abstract class - abstract methods
	- inheritance
	- mixin class
	- inheritancec from built-in objects
	- multi inheritance
	- access levels in class
	- decorator property
	- methods types in class
	+ magic-special methods [built-in] in class
		- __del__
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



# unit_test

	- general
	- doctest module
	- unittest module
	- nose module
	- pytest module
	- selenium module



# debugging

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



# benchmarking

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



[DJANGO]

# launch
	- config settings for launch
	- delete static settings from main urls.py
	- upload django project on server


# general
	- general points
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
	+ CBV : class base view
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



# authentication
	- points of auth
	-[NOT USE] use default User-model-class
	-[NOT USE] relation one-to-one with default User-model-class
	- custom User-model-class
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





















# modules
	- ...



[DJANGO MODULES]








# django-filter module



"""
