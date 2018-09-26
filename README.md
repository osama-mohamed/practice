# [Blog Express](https://blog-nodejs-by-osama-mohamed.herokuapp.com) By Express, Mongoose.

[<img src="https://nodejs.org/static/images/logos/nodejs-new-pantone-black.png" width="200" title="Blog Express" >](https://blog-nodejs-by-osama-mohamed.herokuapp.com)
[<img src="https://webassets.mongodb.com/_com_assets/cms/mongodb-logo-rgb-j6w271g1xn.jpg" width="250" title="Blog Express" >](https://blog-nodejs-by-osama-mohamed.herokuapp.com)

## For live preview :
> [Blog Express](https://blog-nodejs-by-osama-mohamed.herokuapp.com)


## Blog Express website contains:
* User register 
* User login
* User logout 
* Add article
* Edit article
* Delete article


## Usage :
### Run project by :

``` javascript

# run 

1. npm i

2. bower install bootstrap

3. bower install jquery

4. npm start

```

That's it.

## Done :

Now the project is running at `http://localhost:3000` and your routes is:


| Route                                                      | HTTP Method 	   | Description                           	      |
|:-----------------------------------------------------------|:----------------|:---------------------------------------------|
| {host}       	                                             | GET       	     | Home page                                    |
| {host}/articles/add  	                                     | GET        	   | User show add article form                   |
| {host}/articles/add              	                         | POST       	   | User add article                             |
| {host}/articles/{id}/                        	             | GET       	     | Article detail                               |
| {host}/articles/edit/{id}  	                               | GET        	   | User show edit article form                  |
| {host}/articles/edit/{id}                                  | POST       	   | User edit article                            |
| {host}/articles/delete/{id}                                | DELETE      	   | User delete article                          |
| {host}/users/register                        	             | GET      	     | User register show form                      |
| {host}/users/register                        	             | POST      	     | User register                                |
| {host}/users/login                           	             | GET        	   | User login show form                         |
| {host}/users/login                           	             | POST       	   | User login                                   |
| {host}/users/logout                          	             | GET         	   | User logout                                  |



For detailed explanation on how project work, read the [Node Docs](https://nodejs.org/en/docs/), [Express Docs](http://expressjs.com/en/guide/routing.html) and [MongoDB Docs](https://docs.mongodb.com/)

## Developer
This project made by [Osama Mohamed](https://www.facebook.com/osama.mohamed.ms)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)

