# [E-Commerce](https://buysell-by-osama-mohamed.herokuapp.com) By Flask

[<img src="https://www.djangoproject.com/s/img/logos/django-logo-negative.png" width="200" title="E-Commerce" >](https://buysell-by-osama-mohamed.herokuapp.com)
[<img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" width="150" title="E-Commerce" >](https://buysell-by-osama-mohamed.herokuapp.com)


## For live preview :
> [E-Commerce](https://buysell-by-osama-mohamed.herokuapp.com)


## E-commerce website containes:
* User register 
* User login
* User logout 
* Change password
* Reset password
* User delete account
* Order products
* Edit order quantity
* Delete order
* Add review to products
* Calculate avg to every product
* Contact us message



## Usage :
### Run project by :

``` python

# change database connection information in settings.py DATABASES default values with your info then run 

1. export FLASK_APP=buy_sell.py

2. python -m flask run

# OR you can use

1. export FLASK_APP=buy_sell.py

2. flask run

```

That's it.

## Done :

Now the project is running at `http://localhost:8000` and your routes is:


| Route                                                      | HTTP Method 	   | Description                           	      |
|:-----------------------------------------------------------|:----------------|:---------------------------------------------|
| {host}       	                                             | GET       	     | Home page                                    |
| {host}/contact_us                                          | POST     	     | Contact us message                           |
| {host}/products_price_range                                | POST     	     | Search products by price range               |
| {host}/products/{id}                                       | POST     	     | All products page                            |
| {host}/user_forget_password                                | GET      	     | Forget password page                         |
| {host}/user_forget_password_email                          | POST     	     | Send reset password e-mail                   |
| {host}//user_reset_password/{id}/{random_for_reset}        | POST     	     | Enter new password                           |
| {host}/user_register                                       | POST     	     | User register                                |
| {host}/user_login                                          | POST     	     | User login                                   |
| {host}/user_logout                                         | GET     	       | User logout                                  |
| {host}/user_account                                        | GET     	       | User profile                                 |
| {host}/user_profile_picture                                | POST     	     | Change user profile image                    |
| {host}/user_change_password/                               | POST     	     | User change password                         |
| {host}/delete_user_account                                 | POST    	       | Delete user account                          |
| {host}/add_product_to_cart/{id}                            | POST     	     | Add order to cart                            |
| {host}/add_product_to_cart_from_slider/{id}                | POST     	     | Add order to cart from slider                |
| {host}/increase_cart_product_quantity/{id}                 | POST     	     | Increase order quantity                      |
| {host}/edit_cart_product_quantity/{id}                     | POST     	     | Enter order quantity                         |
| {host}/decrease_cart_product_quantity/{id}                 | POST     	     | Decrease order quantity                      |
| {host}/delete_product_from_cart/{id}                       | POST     	     | Delete order                                 |
| {host}/add_to_cart                                         | POST   	       | Cart                                         |
| {host}/buy                                                 | POST     	     | Buy orders                                   |
| {host}/product_review/{id}                                 | POST     	     | Add product review                           |
| {host}/slider_product_review/{id}                          | POST     	     | Add slider product review                    |
| {host}/preview_production/{id}                             | GET     	       | Product detail                               |
| {host}/preview_production_slider/{id}                      | GET     	       | Slider Product detail                        |
| {host}/categories/{category}                               | GET     	       | Search products by category                  |
| {host}/user_search                                         | POST     	     | Search in products name                      |




For detailed explanation on how project work, read the [Flask Docs](http://flask.pocoo.org/docs/0.12/) and [MySQLDB Docs](https://dev.mysql.com/doc/)

## Developer
This project made by [Osama Mohamed](https://www.facebook.com/osama.mohamed.ms)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
