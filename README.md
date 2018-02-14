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
| {host}       	                                             | GET       	   | Home page                                    |
| {host}/admin/  	                                         | GET      	   | Admin control panel                     	  |
| {host}/accounts/register/                                  | POST      	   | User register           	                  |
| {host}/accounts/activate/{code}/                           | GET      	   | Activate user account after register         |
| {host}/accounts/login/                                     | POST      	   | User login           	                      |
| {host}/accounts/logout/                                    | GET      	   | User logout           	                      |
| {host}/accounts/change_password/                           | POST      	   | User change password           	          |
| {host}/accounts/profile/                                   | GET      	   | User profile          	                      |
| {host}/accounts/profile/update/{pk}/                       | PUT      	   | User update checkout information             |
| {host}/accounts/profile/delete/                            | POST      	   | User delete account           	              |
| {host}/accounts/reset_password/                            | POST      	   | User email           	                      |
| {host}/accounts/reset_password/done/                       | POST      	   | Send reset password email           	      |
| {host}/accounts/reset_password/confirm/{uidb64}/{token}/   | POST      	   | Enter new password           	              |
| {host}/accounts/reset_password/complete/                   | POST      	   | Finish reset password           	          |
| {host}/products/                                           | POST      	   | Products page          	                  |
| {host}/products/category/{category}/                       | GET      	   | Search products by category          	      |
| {host}/products/all/                                       | GET      	   | All products           	                  |
| {host}/products/{slug}/                                    | GET      	   | Product detail           	                  |
| {host}/orders/order/{id}/                                  | POST      	   | Order product           	                  |
| {host}/orders/order/{pk}/update/                           | POST      	   | Update order quantity           	          |
| {host}/orders/order/{id}/delete/                           | POST      	   | Delete order           	                  |
| {host}/orders/cart/                                        | GET      	   | Cart page           	                      |
| {host}/orders/pending/                                     | GET      	   | Pending orders           	                  |
| {host}/orders/rejected/                                    | GET      	   | Rejected orders           	                  |
| {host}/orders/accepted/                                    | GET      	   | Accepted orders           	                  |
| {host}/orders/buy/                                         | POST      	   | Buy orders          	                      |
| {host}/orders/thank_you/                                   | GET      	   | Thank you page          	                  |
| {host}/reviews/add_review/{id}/                            | POST      	   | Add review           	                      |
| {host}/reviews/update_review/{id}/                         | POST      	   | Update review           	                  |
| {host}/reviews/delete_review/{id}/                         | POST      	   | Delete review           	                  |
| {host}/contact_us/                                         | POST      	   | Contact us message           	              |


For detailed explanation on how project work, read the [Flask Docs](http://flask.pocoo.org/docs/0.12/) and [MySQLDB Docs](https://dev.mysql.com/doc/)

## Developer
This project made by [Osama Mohamed](https://www.facebook.com/osama.mohamed.ms)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
