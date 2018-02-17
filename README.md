# [Restful API](https://restful-ajax-osama-mohamed.herokuapp.com) By Flask

[<img src="http://flask.pocoo.org/static/logo/flask.png" width="200" title="Restful API" >](https://restful-ajax-osama-mohamed.herokuapp.com)
[<img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" width="150" title="Restful API" >](https://restful-ajax-osama-mohamed.herokuapp.com)


## For live preview :
> [Restful API](https://restful-ajax-osama-mohamed.herokuapp.com)


## Restful API website contains:
* User register 
* User login
* User logout 
* User profile
* Add product
* Edit product
* Delete product
* All products
* Product detail


## Usage :
### Run project by :

``` python

# run 

1. export FLASK_APP=restful_api.py

2. python -m flask run

# OR you can use

1. export FLASK_APP=restful_api.py

2. flask run

```

That's it.

## Done :

Now the project is running at `http://localhost:5000` and your routes is:


| API Route                                                  | HTTP Method 	   | Description                           	      |
|:-----------------------------------------------------------|:----------------|:---------------------------------------------|
| {host}       	                                             | GET       	     | Home page                                    |
| {host}/api/add_product                                     | POST     	     | Add product                                  |
| {host}/api/edit_product/{id}                               | PUT      	     | Edit product                                 |
| {host}/api/delete_product/{id}                             | DELETE    	     | Delete product                               |
| {host}/api/all_products                                    | GET      	     | All products                                 |
| {host}/api/product/{id}                                    | POST      	     | Product detail                               |
| {host}/api/categories/{category}                           | POST     	     | Search products by category                  |
| {host}/users/register                                      | POST      	     | User register                                |
| {host}/users/login                                         | POST     	     | User login                                   |
| {host}/users/profile                                       | POST     	     | User profile                                 |


For detailed explanation on how project work, read the [Flask Docs](http://flask.pocoo.org/docs/0.12/) and [MySQLDB Docs](https://dev.mysql.com/doc/)

## Developer
This project made by [Osama Mohamed](https://www.facebook.com/osama.mohamed.ms)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
