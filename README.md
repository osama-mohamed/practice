# [Shorten URL](https://url-osama-mohamed.herokuapp.com) By Flask and Mongodb

[<img src="https://flask.palletsprojects.com/en/3.0.x/_images/flask-horizontal.png" width="200" title="Shorten URL" >](https://url-osama-mohamed.herokuapp.com)
[<img src="https://webassets.mongodb.com/_com_assets/cms/mongodb-logo-rgb-j6w271g1xn.jpg" width="250" title="Shorten URL" >](https://url-osama-mohamed.herokuapp.com)


## For live preview :
> [Shorten URL](https://url-osama-mohamed.herokuapp.com)


## Usage :
### Run project by :

``` python

# run 

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


For detailed explanation on how project work, read the [Flask Docs](http://flask.pocoo.org/docs/0.12/) and [MongoDB Docs](https://docs.mongodb.com/)

## Developer
This project made by [Osama Mohamed](https://www.linkedin.com/in/osama-mohamed-ms/)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
