# [Github Comparison with Bulma](https://github-compare-osama-mohamed.herokuapp.com) By Django

[<img src="https://www.djangoproject.com/s/img/logos/django-logo-negative.png" width="200" title="Github Comparison" >](https://github-compare-osama-mohamed.herokuapp.com)
[<img src="https://raw.githubusercontent.com/jgthms/bulma/master/docs/images/bulma-banner.png" width="200" title="Github Comparison" >](https://github-compare-osama-mohamed.herokuapp.com)


## For live preview :
> [Github Comparison](https://github-compare-osama-mohamed.herokuapp.com)


## Github Comparison website contains:
* 2 Users Comparison

## Note:
All Data comes from [https://api.github.com](https://api.github.com) using github.com API Services


## Usage :
### Run project by :

``` python

# change database connection information in settings.py DATABASES default values with your info then run 

1. python manage.py migrate

2. python manage.py runserver

# if you want to manage to project just create super user account by :

3. python manage.py createsuperuser

```

That's it.

## Done :

Now the project is running at `http://localhost:8000` and your routes is:


| Route                                                      | HTTP Method 	   | Description                           	      |
|:-----------------------------------------------------------|:----------------|:---------------------------------------------|
| {host}       	                                             | POST      	     | Home page                                    |
| {host}/api/  	                                             | POST      	     | Home page in API                             |


For detailed explanation on how project work, read the [Django Docs](https://docs.djangoproject.com/en/1.11/) and [MySQLDB Docs](https://dev.mysql.com/doc/)

## Developer
This project made by [Osama Mohamed](https://www.facebook.com/osama.mohamed.ms)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
