# Multi Tenant Architecture using multiple database with Django

## Cloning and Initial setup

### Clone the repo.


### Create virtual environment 
```shell
virtualenv venv
```

#### For different Python version [In this Example, python3.9]
```shell
virtualenv venv -p python3.9
```

### Activate the virtual environment
#### For linux
```shell
source venv/bin/activate
```

#### For windows:

```shell
source venv/Scripts/activate
```

## Install Dependencies

```shell
pip install -r requirements.txt
```

For Other Python version [In this Example, python3.9]

```shell
pip3.9 install -r requirements.txt
```

## Create and update environment file
### Copy the .env.example file as .env and update the details

## Database configurations in .env file

```python
DATABASES={"default":{"ENGINE":"django.db.backends.sqlite3","NAME":"db.sqlite3"},"outcodeNepal":{"ENGINE":"django.db.backends.sqlite3","NAME":"db.outcodeNepal"},"outcodePeru":{"ENGINE":"django.db.backends.sqlite3","NAME":"db.outcodePeru"}}
```
This configuration is the example database configuration for sqlite3.
You can update the database configuration for other database engines as well.

<p>Since, we will be using the multiple database, we will be using the dict format in .env file for all the databases</p>

## Hosts configurations

### Update the hostnames in the hosts in */etc/hosts*
```shell
127.0.0.1 office.local
127.0.0.1 outcode-nepal.office.local
127.0.0.1 outcode-peru.office.local
```

### Update on *ALLOWED_HOSTS* in *settings.py* file
```python
ALLOWED_HOSTS = ['office.local', '.office.local']
```

## Creating migrations, database schema and create super admin

### Run the command to make migrations
```shell
python manage.py makemigrations Office
```

### For default database
#### Run the command to migrate 
```shell
python manage.py migrate 
```

#### Run the command to migrate for create superuser for default database
```shell
python office_manage.py createsuperuser
```

### For outcodeNepal Tenant
#### Run the command to migrate

User *--database* option to use the respective Tenant
For Tenant **outcodeNepal** use *--database=outcodeNepal*
```shell
python manage.py migrate --database=outcodeNepal
```

User *--database* option to use the respective Tenant
For Tenant **outcodeNepal** use *--database=outcodeNepal*

#### Run the command to migrate for create superuser for Tenant
```shell
python office_manage.py createsuperuser --database=outcodeNepal
```



## Run the server
### Run server for default site
```shell
python manage.py runserver office.local:8000
```
You can use different port


### Run server for outcodeNepal Tenant
```shell
python manage.py runserver outcode-nepal.office.local:8018
```
You can use different port after:


## Accessing Tenant's site and superadmin portal:

### For Default site

```shell
http://office.local:8000/
```

### For Admin site

```shell
http://office.local:8000/admin
```

### For Main site

```shell
http://outcode-nepal.office.local:8018/
```

### For Admin site

```shell
http://outcode-nepal.office.local:8018/admin
```

## Check the issue in the app:
    ` ./manage.py check`

## Copyright

Copyright (C) 2020 [Outcode Software](https://www.outcodesoftware.com/).
