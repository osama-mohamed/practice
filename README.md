# [Blog](https://blog-by-osama-mohamed.herokuapp.com) By Flask

[<img src="http://flask.pocoo.org/static/logo/flask.png" width="200" title="Blog" >](https://blog-by-osama-mohamed.herokuapp.com)
[<img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" width="150" title="Blog" >](https://blog-by-osama-mohamed.herokuapp.com)


## For live preview :
> [Blog](https://blog-by-osama-mohamed.herokuapp.com)


## Blog website containes:
* User register 
* User login
* User logout 
* Delete user account
* Add article
* Edit article
* Delete article
* Display images
* URL shortener


## Usage :
### Run project by :

``` python

# change database connection information in settings.py DATABASES default values with your info then run 

1. export FLASK_APP=osama_blog.py

2. python -m flask run

# OR you can use

1. export FLASK_APP=osama_blog.py

2. flask run

```

That's it.

## Done :

Now the project is running at `http://localhost:5000` and your routes is:


| Route                                                      | HTTP Method 	   | Description                           	      |
|:-----------------------------------------------------------|:----------------|:---------------------------------------------|
| {host}       	                                             | GET       	     | Home page                                    |

| {host}/result       	                                     | POST       	   | show url shortener result                    |
| {host}/redirect/{url_name}       	                         | POST       	   | Redirect to the original link                |
| {host}/about 	                                             | GET       	     | About me page                                |
| {host}/search 	                                           | POST      	     | Search in article author, title and id       |
| {host}/articles       	                                   | GET       	     | all articles page                            |
| {host}/article/{id}/                        	             | GET       	     | Article detail                               |
| {host}/categories                                          | POST       	   | Show articles by category page               |
| {host}/search_by_categories/{category}       	             | GET       	     | search articles by category page             |
| {host}/article_picture/{id}/{picture_name}                 | GET         	   | Show article image from dashboard            |
| {host}/article_picture_inner/{id}/{user_name}/{pic}        | GET         	   | Show article image from article page         |
| {host}/profile_picture/{pic}                	             | GET       	     | Show user profile picture                    |
| {host}/forget_password                             	       | POST      	     | User forget password                         |
| {host}/reset_password                             	       | POST      	     | Send reset password e-mail                   |
| {host}/reset/{id}                             	           | GET      	     | Enter new password                           |
| {host}/reset_password2                             	       | POST      	     | Finish reset password                        |
| {host}/register                             	             | POST      	     | User register                                |
| {host}/login                                	             | POST       	   | User login                                   |
| {host}/logout                                	             | GET         	   | User logout                                  |
| {host}/dashboard                            	             | GET       	     | User profile                                 |
| {host}/upload                               	             | POST      	     | Upload user profile picture                  |
| {host}/delete_file                           	             | POST      	     | Delete user profile picture                  |
| {host}/add_article                          	             | POST      	     | User add article                             |
| {host}/upload_file_article                   	             | POST      	     | User upload article picture                  |
| {host}/delete_article_file                   	             | POST      	     | Delete upload article picture                |
| {host}/edit_article/{id}                          	       | POST      	     | User Edit article                            |
| {host}/delete_article/{id}                   	             | POST      	     | User delete article                          |
| {host}/delete_all_articles                   	             | POST      	     | User delete all articles                     |
| {host}/delete_account                       	             | POST      	     | User delete account                          |


For detailed explanation on how project work, read the [Flask Docs](http://flask.pocoo.org/docs/0.12/) and [MySQLDB Docs](https://dev.mysql.com/doc/)

## Developer
This project made by [Osama Mohamed](https://www.facebook.com/osama.mohamed.ms)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)# Blog
