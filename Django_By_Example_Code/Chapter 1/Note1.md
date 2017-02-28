```
django-admin startproject mysite

cd mysite
python manage.py migrate

python manage.py runserver
python manage.py runserver 127.0.0.1:8001 --settings=mysite.settings

python manage.py startapp blog
```


Since we are going to deal with datetimes, we will install the pytz
module.This module provides timezone definitions for Python and is
required by SQLite to work with datetimes. Open the shell and install
pytz with the following command:
```
pip install pytz
```
Django comes with support for timezone-aware datetimes. You can activate
/deactivate time zone support with the USE_TZ setting in the settings.py
 file of your project. This setting is set to True when you create a new
  project using the startproject management command.


```
python manage.py createsuperuser

python manage.py makemigrations blog
```


Let's take a look at the SQL code that Django will execute in the
database to create the table for our model. The sqlmigrate command takes
 migration names and returns their SQL without running it. Run the
 following command to inspect its output:
 ```
 python manage.py sqlmigrate blog 0001
 ```

```
python manage.py migrate

python manage.py createsuperuser
```


