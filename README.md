# [Btre](https://osama-btre-django.herokuapp.com) By Django 2.1

[<img src="https://www.djangoproject.com/s/img/logos/django-logo-negative.png" width="200" title="Btre" >](https://osama-btre-django.herokuapp.com)
[<img src="https://www.osamamohamed.com/img/icons/svg/postgresql/postgresql.svg" width="100" title="Btre" >](https://osama-btre-django.herokuapp.com)


## For live preview :
> [Btre](https://osama-btre-django.herokuapp.com)


## Btre website contains:
### 5 Apps :
    1. Accounts
    2. Contacts
    3. Realtors
    4. Listings
    5. Pages


* User register 
* User login
* User logout 
* User dashboard
* Listings page
* Listing detail
* Listings search
* Make inquiry -auto fill if user logged in-
* Seller of month


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


| Route                                                      | HTTP Method         | Description                           	    |
|:-----------------------------------------------------------|:--------------------|:---------------------------------------------|
| {host}       	                                             | GET       	       | Home page                                    |
| {host}/admin/  	                                         | GET      	       | Admin control panel                          |
| {host}/about/  	                                         | GET      	       | About page                                   |
| {host}/accounts/register/                                  | POST       	       | User register             	                  |
| {host}/accounts/login/                                     | POST      	       | User login                	                  |
| {host}/accounts/logout/                                    | POST      	       | User logout              	                  |
| {host}/accounts/dashboard/                                 | GET      	       | User dashboard           	                  |
| {host}/listings/                                           | GET      	       | Listings page            	                  |
| {host}/listings/{listing_id}/                              | GET      	       | Listing detail           	                  |
| {host}/listings/search/                                    | GET      	       | Listings search        	                  |
| {host}/contacts/contact/                                   | POST      	       | Make inquiry              	                  |



For detailed explanation on how project work, read the [Django Docs](https://docs.djangoproject.com/en/2.1/) and [Postgresq Docs](https://www.postgresql.org/docs)

## Developer
This project made by [Osama Mohamed](https://www.facebook.com/osama.mohamed.ms)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
