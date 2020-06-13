# Project Title

## fury-backend-python Web Application

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development purpose.

### Prerequisites

    Python 3.6.9
<<<<<<< HEAD
=======
    Pip @Latest
>>>>>>> f25b57ac1ff66bf1d3a7cd067af7ddbd7f7553d7

### Installing

You'll need to have a virtual environment installed on your machine

    pip3 install virtualenv
<<<<<<< HEAD

=======
### Go to the directory where the manage.py file is located
>>>>>>> f25b57ac1ff66bf1d3a7cd067af7ddbd7f7553d7
Setup virtual environment

    virtualenv -p python3.6 .virtualenv

Activate virtual environment

    source .virtualenv/bin/activate

Install the requirements

    pip install -r requirements


<<<<<<< HEAD
Configuring the settings

    Navigate to settings.py inside and change setting
=======
If there are any errors try installing the packages manually:
- Update python to latest \n
- Update pip \n
- pip install django
-pip install django_rest_framework
Debug the rest :-#

    
>>>>>>> f25b57ac1ff66bf1d3a7cd067af7ddbd7f7553d7

Make migrations, createsuperuser and run the server

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

### Built With

    Python - Programming language used
<<<<<<< HEAD
    django-rest-swagger - Used to generate documentation for all the endpoints
=======
    django-rest-swagger - Used to generate documentation for all the endpoints
### End Points   

-/v1/documentation:
-/v1/account
-/v1/task
>>>>>>> f25b57ac1ff66bf1d3a7cd067af7ddbd7f7553d7
