# Setup Process

## Create a virtual env in your system

- Command to install venv in linux

  ```bash
  apt install python3.8-venv
  ```

- Create a venv name env

  ```bash
  python3 -m venv env
  ```

- activate the env

  ```bash
  source env/bin/activate
  ```

## Setup project for django

- check for pip (python installeer program)

  ```bash
  pip --version
  ```

- install django

  ```bash
  pip install django
  ```

- Install django rest framework

  ```bash
  pip install djangorestframework
  ```

- Crerate a new django project using django Admin

  ```bash
  django-admin startproject BasicDRF
  ```

- Change directory to django project

  ```bash
  cd incomexpensesapi/
  ```

- Create you app inside your project

  ```bash
  python3 manage.py startapp api_basic
  ```

- Register your app and rest_framework app too inside setting.py in you project root file

  ```py
  INSTALLED_APPS = [
      'django.contrib.admin',
      ............ ,
      .............,
      'api_basic',
      'rest_framework'
  ]
  ```

- Before runnig the server it is good practice to save all the changes using

  ```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

- Then inside your project folder using manage.py file run the server 0n port no :8000

  ```bash
  python3 manage.py runserver
  ```

- Then Create a super user such that we cal login to admin pannel

```bash
python3 manage.py createsuperuser
```

**Our basic setup is complete know let's code :)**

---
