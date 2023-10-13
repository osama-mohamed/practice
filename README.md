# [Restful API with Ajax](https://restful-ajax-osama-mohamed-dj.herokuapp.com) By Django

[<img src="https://www.djangoproject.com/s/img/logos/django-logo-negative.png" width="200" title="Restful API with Ajax" >](https://restful-ajax-osama-mohamed-dj.herokuapp.com)
[<img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" width="150" title="Restful API with Ajax" >](https://restful-ajax-osama-mohamed-dj.herokuapp.com)




## For live preview :
> [Restful API with Ajax](https://restful-ajax-osama-mohamed-dj.herokuapp.com)


## Restful API with Ajax website contains:
### 2 Apps :
    1. Accounts
    2. Products
* User register 
* User login
* Add product
* Edit product
* Delete product
* All products
* Product detail

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

| API Route                                                  | HTTP Method 	   | Description                           	      |
|:-----------------------------------------------------------|:----------------|:---------------------------------------------|
| {host}       	                                             | GET       	     | Home page                                    |
| {host}/admin/	                                             | GET       	     | Admin control panel                          |
| {host}/api/products/{slug}/                                | GET      	     | Product Detail                               |
| {host}/api/products/all/                                   | GET      	     | All products                                 |
| {host}/api/products/category/{category}/                   | GET      	     | Search products by category                  |
| {host}/api/products/add/                                   | POST     	     | Add product                                  |
| {host}/api/products/update/{id}/                           | PUT      	     | Update product                               |
| {host}/api/products/delete/{id}/                           | DELETE    	     | Delete product                               |
| {host}/api/accounts/register/                              | POST      	     | User register                                |
| {host}/api/accounts/login/                                 | POST     	     | User login                                   |


For detailed explanation on how project work, read the [Django Docs](https://docs.djangoproject.com/en/1.11/) and [MySQLDB Docs](https://dev.mysql.com/doc/)

## Developer
This project made by [Osama Mohamed](https://www.linkedin.com/in/osama-mohamed-ms/)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
