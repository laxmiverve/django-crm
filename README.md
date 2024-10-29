# Django CRM Application

## Virtual Environment

- `pipenv shell` -> To activate virtual envirnoment. If virtual environment is not there it automatically create a new one.
- `deactivate` -> To deactivate virtual envirnoment

When you create a virtual envirnoment in python. Whatever you installed in virtual envirnoment is totally isolated from your local envirnoment.

## Create a Django Project

- `django-admin startproject < project_name >` -> To create a project in django . in my case my project name is django-crm
- `python manage.py runserver` -> To run the Django project
- `python manage.py runserver < port_number >` -> To run on a specific port. By default django run on port 8000.
- `python manage.py startapp < app_name >` -> To create an app. In a Django project you can create multiple app.
  in my case my app name is demoApp

## Project Structure

```
 `myProject/` ----> root directory is a container for your project. you can rename it
    `manage.py` ----> command-line utility that lets you interact with this Django project
    `myProject/` ----> actual Python package for your project
        `init.py` ----> An empty file that tells Python that this directory should be considered a Python package
        `settings.py` ----> configuration for this Django project.
        `urls.py` -----> All urls are configured here. It also used to transfer the control to the url.py of app
        `asgi.py`
        `wsgi.py`
```

Remember: When you use the command startapp to only creates the app file. And the main project did not aware of this.
So you have to add the app in the main project. To do this you have to add
`<app_name>` in the INSTALLED_APPS in the settings.py file.

## Database

- `python manage.py migrate` --> Migrate all files
- `python manage.py createsuperuser` --> Create a super user
- `db.sqlite3` -> Default database used in django

## Files

- `views.py` file -> Like a controller file. Whatever the functionality and business logics are written here. This file is always send the response

- `models.py` -> Where we write the all database models

- `static/` -> in static folder all CSS and JavaScripts are wtitten
- `templates/` -> in templates are HTML are written
- `media/` -> in media folder all images are written

## When you write the demoApp model, Django did not know about your already created a model. For this to run some commands:

- `python manage.py makemigrations` --> To create migrations
- `python manage.py migrate` --> To migrate the database

## To see the migration status

- `python manage.py sqlmigrate <app_name> <migration_name>` --> To see the sql
- `python manage.py showmigrations` --> To see the migration status

## ERROR: django.template.exceptions.TemplateDoesNotExist: index.html

- Before render a html page the directory is must added in `settings.py` file.
- TEMPLATES -> DIRS": ['templates']

## To inject CSS in django :

1. Add href="{% static 'style.css' %}"> in html file
2. Add STATICFILES_DIRS = [BASE_DIR / "static"] in settings.py file

## Tailwind CSS

Add tailwind in Django project by using below command:

- `pip install django-tailwind`
- `pip install 'django-tailwind[reload]'`
- `python manage.py tailwind init`
- `python manage.py tailwind install`
- `python manage.py tailwind start`

## IP Hosting:

ALLOWED_HOSTS = ["192.168.1.53", 'localhost', '127.0.0.1']

`python manage.py runserver 192.168.1.53:8000` -> Run it on terminal
