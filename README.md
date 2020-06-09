# Project Title

## fury-backend-python Web Application

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development purpose.

### Prerequisites

    Python 3.6.9

### Installing

You'll need to have a virtual environment installed on your machine

    pip3 install virtualenv

Setup virtual environment

    virtualenv -p python3.6 .virtualenv

Activate virtual environment

    source .virtualenv/bin/activate

Install the requirements

    pip install -r requirements


Configuring the settings

    Navigate to settings.py inside and change setting

Make migrations, createsuperuser and run the server

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

### Built With

    Python - Programming language used
    django-rest-swagger - Used to generate documentation for all the endpoints