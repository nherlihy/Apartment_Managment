# Added a test group file
Run the following to update the database

```sh
$ python manage.py flush
$ python manage.py makemigrations
$ python manage.py migrate 
$ python manage.py shell
>>> execfile('dbtest.py')
```

Once you do this, there will be a user for each of our names with default password of 'wit'

