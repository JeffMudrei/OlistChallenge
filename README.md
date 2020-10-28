# Product Registration System

It allows the registration of products with information of: Price, Category, Name and description.

## It's possible:
Add new products.
Delete existing products.
Change existing products.

Developed with Python and Django framework.

## To use:
You will need Python installed. For more information: [Python Official Website](https://www.python.org/)

### To activate the virtual environment called 'myenv':

Navigate with your terminal to the main project folder, then use the command:
```
$ source myenv / bin / activate
```
You will know it is inside the virtual evironment if your terminal has **(myenv)** at the beginning of the line, it will look like this:
```
(myenv) jeffmudrei @ JeffMudrei: ~ / product_categorie $
```
### The following commands create the database:
```
$ python manage.py makemigrations
$ python manage.py migrate

```
### Creating an admin user
Type it:
```
$ python manage.py createsuperuser

```
Then enter a user, email and password to access the system admin.

## To upload the server:

With myenv enabled, and in the project's root folder, type the following command:
```
$ python manage.py runserver
```
### A message like this should be displayed:
```
Watching for file changes with StatReloader
Performing system checks ...

System check identified no issues (0 silenced).
October 28, 2020 - 17:25:54
Django version 3.1.2, using settings 'product_categories.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Open your browser, we use Mozilla Firefox, and type the url:

http://127.0.0.1:8000/

To access the admin:

http://127.0.0.1:8000/admin/

Use the categories.csv file to register the categories and test the system.

Thank you!

