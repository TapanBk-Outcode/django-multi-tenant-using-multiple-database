# Multi Tenant Architecture using multiple database with Django

## Installation

### Clone the repo.


### Create virtual environment 
```shell
virtualenv venv
```

#### For different Python version
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

```shell
pip3 install -r requirements.txt
```


## Database configuration
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'outcodeNepal': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.outcodeNepal',
    },
    'outcodePeru': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.outcodePeru',
    },
}
```

## Hosts configuration

### Update the hostnames in the hosts in */etc/hosts*
```shell
127.0.0.1 office.local
127.0.0.1 outcode-nepal.office.local
127.0.0.1 outcode-peru.office.local
```

### Update on ALLOWED_HOSTS in *settings.py* file
```python
ALLOWED_HOSTS = ['office.local', '.office.local']
```

## Migrations

### Run the command to make migrations
```shell
python manage.py makemigrations Office
```

### For default database
#### Run the command to migrate 
```shell
python manage.py migrate 
```

### Run the command to migrate for create superuser for default database
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

#### Run the command to migrate for create superuser
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


## Accessing Tenant:

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
