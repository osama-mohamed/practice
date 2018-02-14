# shorten_url By Flask

[<img src="http://flask.pocoo.org/static/logo/flask.png" width="200" title="E-Commerce" >](https://www.facebook.com/osama.mohamed.ms)
[<img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" width="150" title="E-Commerce" >](https://www.facebook.com/osama.mohamed.ms)


## Usage :
### Run project by :

``` python

# change database connection information in settings.py DATABASES default values with your info then run 

1. export FLASK_APP=url_short.py

2. python -m flask run

# OR you can use

1. export FLASK_APP=url_short.py

2. flask run

```

That's it.

## Done :

Now the project is running at `http://localhost:5000` and your routes is:


| Route                                                      | HTTP Method 	   | Description                           	      |
|:-----------------------------------------------------------|:----------------|:---------------------------------------------|
| {host}       	                                             | GET       	     | Home page                                    |
| {host}/result       	                                     | POST       	   | Show url shortener result                    |
| {host}/{url_name}               	                         | POST       	   | Redirect to the original link                |


For detailed explanation on how project work, read the [Flask Docs](http://flask.pocoo.org/docs/0.12/) and [MySQLDB Docs](https://dev.mysql.com/doc/)

## Developer
This project made by [Osama Mohamed](https://www.facebook.com/osama.mohamed.ms)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
