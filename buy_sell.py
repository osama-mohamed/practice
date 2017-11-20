# some imports
from flask import Flask, render_template, flash, redirect, url_for, session, request, send_from_directory
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, validators, FileField, IntegerField, PasswordField
from passlib.hash import sha256_crypt
from werkzeug.utils import secure_filename
from shutil import rmtree, copyfile, copy2, copy, copyfileobj
from functools import wraps
from flask_mail import Mail, Message
import MySQLdb
import os


# connect to database in localhost to create database and their tables

database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
# cursor.execute("DROP DATABASE IF EXISTS buy_sell;")
cursor.execute("CREATE DATABASE IF NOT EXISTS buy_sell DEFAULT CHARSET UTF8")
database.select_db('buy_sell')
# cursor.execute("DROP TABLE IF EXISTS users;")
# cursor.execute("DROP TABLE IF EXISTS categories;")
# cursor.execute("DROP TABLE IF EXISTS products;")
# cursor.execute("DROP TABLE IF EXISTS slider_products;")
# cursor.execute("DROP TABLE IF EXISTS buy_orders;")
# cursor.execute("DROP TABLE IF EXISTS orders;")
# cursor.execute("DROP TABLE IF EXISTS reviews;")


cursor.execute("CREATE TABLE IF NOT EXISTS users(\
                id INT(11) AUTO_INCREMENT PRIMARY KEY,\
                permission VARCHAR(10) NOT NULL,\
                first_name VARCHAR(100) NOT NULL,\
                last_name VARCHAR(100) NOT NULL,\
                email VARCHAR(100) NOT NULL,\
                gender VARCHAR(10) NOT NULL,\
                country VARCHAR(50) NOT NULL,\
                username VARCHAR(100) NOT NULL,\
                password VARCHAR(100) NOT NULL,\
                files TEXT NOT NULL,\
                register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP );")

cursor.execute("CREATE TABLE IF NOT EXISTS products(\
                id INT(11) AUTO_INCREMENT PRIMARY KEY,\
                category VARCHAR(100) NOT NULL,\
                number_of_sales INT(11) NOT NULL,\
                number_of_views INT(11) NOT NULL,\
                product_name VARCHAR(255) NOT NULL,\
                description TEXT NOT NULL,\
                price INT(10) NOT NULL,\
                discount FLOAT NOT NULL,\
                files TEXT NOT NULL,\
                create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")

cursor.execute("CREATE TABLE IF NOT EXISTS slider_products(\
                id INT(11) AUTO_INCREMENT PRIMARY KEY,\
                category VARCHAR(100) NOT NULL,\
                number_of_sales INT(11) NOT NULL,\
                number_of_views INT(11) NOT NULL,\
                product_name VARCHAR(255) NOT NULL,\
                description TEXT NOT NULL,\
                price INT(10) NOT NULL,\
                discount FLOAT NOT NULL,\
                files TEXT NOT NULL,\
                create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")

cursor.execute("CREATE TABLE IF NOT EXISTS categories (category VARCHAR(255) PRIMARY KEY);")

cursor.execute("CREATE TABLE IF NOT EXISTS orders(\
                id INT(11) AUTO_INCREMENT PRIMARY KEY,\
                user_id INT(11) NOT NULL,\
                user_name VARCHAR(255) NOT NULL,\
                status VARCHAR(255) NOT NULL,\
                product_id INT(11) NOT NULL,\
                product_name VARCHAR(255) NOT NULL,\
                quantity INT(11) NOT NULL,\
                price INT(10) NOT NULL,\
                discount FLOAT NOT NULL,\
                files TEXT NOT NULL,\
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")

cursor.execute("CREATE TABLE IF NOT EXISTS reviews(\
                id INT(11) AUTO_INCREMENT PRIMARY KEY,\
                user_id INT(11) NOT NULL,\
                user_name VARCHAR(255) NOT NULL,\
                product_id INT(11) NOT NULL,\
                product_name VARCHAR(255) NOT NULL,\
                rate TINYINT(2) NOT NULL,\
                review TEXT NOT NULL,\
                review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")

cursor.execute("CREATE TABLE IF NOT EXISTS buy_orders(\
                id INT(11) AUTO_INCREMENT PRIMARY KEY,\
                user_id INT(11) NOT NULL,\
                user_name VARCHAR(255) NOT NULL,\
                status VARCHAR(255) NOT NULL,\
                product_id INT(11) NOT NULL,\
                product_name VARCHAR(255) NOT NULL,\
                quantity INT(11) NOT NULL,\
                price INT(10) NOT NULL,\
                discount FLOAT NOT NULL,\
                country VARCHAR(255) NOT NULL,\
                region VARCHAR(255) NOT NULL,\
                address VARCHAR(255) NOT NULL,\
                phone_number VARCHAR(255) NOT NULL,\
                comments TEXT NOT NULL,\
                files TEXT NOT NULL,\
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")


# create default admin account if not exists

result = cursor.execute('SELECT username FROM users WHERE username=%s', ['admin'])
if result > 0:
    pass
else:
    admin_password = sha256_crypt.encrypt(str('admin')) 
    cursor.execute("INSERT INTO users(permission, first_name, last_name,\
             email, gender, country, username, password, files)\
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", \
            ('admin', 'admin', 'admin', 'admin', 'admin', \
             'admin', 'admin', admin_password, 'admin.png'))
    database.commit()
    os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\admin")
    copy(r'C:\Users\OSAMA\Desktop\buy_sell\static\admin.png', r'C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\admin\admin.png')

database.close()


app = Flask(__name__)


# application configuration

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'buy_sell'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


# application configuration to send email with gmail

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'osama.buy.sell@gmail.com'
app.config['MAIL_PASSWORD'] = 'SELLbuyBYOSAMA'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# website icon

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.png', mimetype='image/vnd.microsoft.icon')


# home page

@app.route('/', methods=['post', 'get'])
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM slider_products LIMIT 1")
    slider_products_first = cur.fetchall()
    cur.execute("SELECT * FROM slider_products LIMIT 1 OFFSET 1")
    slider_products_second = cur.fetchall()
    # cur.execute("SELECT * FROM slider_products ORDER BY id DESC LIMIT 1")
    cur.execute("SELECT * FROM slider_products LIMIT 1 OFFSET 2")
    slider_products_third = cur.fetchall()
    cur.execute("SELECT * FROM products ORDER BY id DESC LIMIT 6;")
    latest_products = cur.fetchall()
    cur.execute("SELECT * FROM categories")
    categories = cur.fetchall()
    cur.execute("SELECT * FROM products ORDER BY number_of_views DESC LIMIT 3;")
    recommended_products = cur.fetchall()
    cur.execute("SELECT * FROM products ORDER BY number_of_views DESC LIMIT 3 OFFSET 3")
    recommended_products_second = cur.fetchall()
    # cur.execute("SELECT * FROM products WHERE category = %s ORDER BY id DESC  LIMIT 8;", ['hosting'])
    # latest_productss = cur.fetchall()
    cur.close()
    return render_template('home.html', latest_products=latest_products, categories=categories, slider_products_first=slider_products_first, slider_products_second=slider_products_second, slider_products_third=slider_products_third, recommended_products=recommended_products, recommended_products_second=recommended_products_second)


# all products page
@app.route('/products')
def products():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products ORDER BY id DESC;")
    all_products = cur.fetchall()


    # for product in all_products:
    #     product_name = product['product_name']
    #     print(product_name)
    #     cur.execute("SELECT SUM(rate) / COUNT(product_name) AS avg_rate FROM reviews WHERE product_name = %s;", [product_name])
    #     rate = cur.fetchall()
    #     print(rate)
    cur.close()
    return render_template('all_products.html', all_products=all_products)


# user reset password page

@app.route('/user_forget_password')
def user_forget_password():
    return render_template('user_forget_password.html')


# send e-mail with link to reset user account password

@app.route("/user_forget_password_email", methods=['GET', 'POST'])
def user_forget_password_email():
    if request.form['username_reset'] == '':
        flash('You did not write a username !', 'warning')
        return render_template('user_forget_password.html')
    user_name = request.form['username_reset']
    cur = mysql.connection.cursor()
    r = cur.execute("SELECT id, email, username FROM users WHERE username = %s AND permission='user' ", [user_name])
    res = cur.fetchone()
    if r > 0:
        email = res['email']
        msg = Message()
        msg.sender = 'osama.buy.sell@gmail.com'
        msg.subject = "Reset Your Password"
        msg.recipients = [email]
        msg.body = "Reset Your Password : http://localhost:5000/user_reset_password/%s \n message sent from Flask-Mail Automatic sender!" % (res['id'])
        mail.send(msg)
        flash("The Reset Message has been Sent to your email!", "success")
        flash("Please check your email!", "warning")
        return redirect(url_for('home'))
    else:
        flash("This username Not Found!", "warning")
        return redirect(url_for('home'))


# reset password form validators

class reset_password(Form):
    password = PasswordField('Password',
                             [validators.DataRequired(), validators.Length(min=6, max=100),
                              validators.EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password', [validators.DataRequired()])


# write new password page

@app.route("/user_reset_password/<id>", methods=['GET', 'POST'])
def user_reset_password(id):
    form = reset_password(request.form)
    if request.method == 'POST' and form.validate():
        encrypted_password = sha256_crypt.encrypt(str(form.password.data))
        cur = mysql.connection.cursor()
        cur.execute("UPDATE users SET password = %s WHERE id = %s AND permission='user'", [encrypted_password, id])
        mysql.connection.commit()
        cur.close()
        flash("You Have Successfully Changed Your Password Now!", "success")
        return redirect(url_for('home'))
    return render_template('user_reset_password.html', form=form)


# user part ***********************************************************************************************


# user registration validators form

class RegisterForm(Form):
    first_name = StringField('First Name', [validators.InputRequired()])
    last_name = StringField('Last Name', [validators.InputRequired()])
    username = StringField('User Name', [validators.InputRequired()])
    password = PasswordField('Password',
                             [validators.DataRequired(), validators.Length(min=6, max=100),
                              validators.EqualTo('confirm', message='Passwords Do Not Match')])
    confirm = PasswordField('Confirm Password', [validators.DataRequired()])


# user register page

@app.route('/user_register', methods=['post', 'get'])
def user_register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data

        folder = os.path.exists(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\{}".format(username))
        if folder == True:
            flash('Folder Name Already Exists', 'warning')
            return redirect(url_for('user_register'))

        cur = mysql.connection.cursor()
        cur.execute("SELECT username FROM users WHERE username = %s", [username])
        res = cur.fetchone()
        if username in str(res):
            msg = "User Name Already Exists"
            return render_template('user_register.html', form=form, msg=msg)
        else:
            first_name = form.first_name.data.lower()
            last_name = form.last_name.data.lower()
            email = request.form['email'].lower()
            gender = request.form['gender']
            country = request.form['country']
            username = form.username.data
            password = sha256_crypt.encrypt(str(form.password.data))
            file = request.files['file']
            if file.filename == '':
                flash('You Have to Select a File!', 'warning')
            if file and allowed_file(file.filename):
                try:
                    rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\{}".format(username))
                    os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\{}".format(username))
                except:
                    os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\{}".format(username))
                filename = secure_filename(file.filename)
                dir = r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\{}".format(username)
                file.save(os.path.join(dir, filename))
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO users(permission, first_name, last_name,\
                             email, gender, country, username, password, files)\
                             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", \
                            ("user", first_name, last_name, email, gender,\
                             country, username, password, filename))
                mysql.connection.commit()
                cur.close()
                flash('You Have Created Account successfully!', 'success')
                return redirect(url_for('user_login'))
    return render_template('user_register.html', form=form)


# user login page

@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE username = BINARY %s AND permission='user'", [username])
        if result > 0:
            data = cur.fetchone()
            password = data['password']
            if sha256_crypt.verify(password_candidate, password):
                session['user_logged_in'] = True
                session['user_username'] = username
                cur.close()
                flash('Now You Are Logged In ', 'success')
                return redirect(url_for('user_account'))
            else:
                error = 'Wrong Password!'
                return render_template('user_login.html', error=error)
        else:
            error = 'Username Can Not Be Found!'
            return render_template('user_login.html', error=error)
    return render_template('user_login.html')


# check if user is still logged in 

def is_user_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user_logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please Login', 'danger')
            return redirect(url_for('user_login'))
    return wrap


# user log out

@app.route('/user_logout')
@is_user_logged_in
def user_logout():
    session.clear()
    flash('You Are Now Logged Out', 'success')
    return redirect(url_for('user_login'))


# user account page

@app.route('/user_account', methods=['post', 'get'])
@is_user_logged_in
def user_account():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM buy_orders WHERE user_name = %s", [session['user_username']])
    orders = cur.fetchall()
    cur.execute("SELECT files FROM users WHERE username = %s", [session['user_username']])
    image = cur.fetchone()
    user_image = image['files']
    return render_template('user_account.html', orders=orders, user_image=user_image)


# user registration validators form

class CartbuyForm(Form):
    address = StringField('Address', [validators.InputRequired(), validators.length(min=10, max=200)])
    phone_number = StringField('Phone Number', [validators.InputRequired()])
    comments = TextAreaField('Comments', [validators.InputRequired()])


# cart page

@app.route('/add_to_cart', methods=['post', 'get'])
@is_user_logged_in
def add_to_cart():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM orders WHERE user_name = %s", [session['user_username']])
    orders = cur.fetchall()
    cur.execute("SELECT user_name FROM orders WHERE user_name = %s", [session['user_username']])
    f = cur.fetchall()
    cur.execute("SELECT SUM((price * quantity) - (quantity * discount)) FROM orders WHERE user_name = %s", [session['user_username']])
    # cur.execute("SELECT SUM((price * quantity) - (quantity * discount)) AS total FROM orders WHERE user_name = %s", [session['user_username']])
    order_price = cur.fetchone()
    cur.execute("SELECT SUM(quantity) FROM orders WHERE user_name = %s", [session['user_username']])
    quantities = cur.fetchone()
    cur.close()
    return render_template('cart.html', orders=orders, price=order_price['SUM((price * quantity) - (quantity * discount))'], quantity=quantities['SUM(quantity)'], f=f)


# buy orders page

@app.route('/buy', methods=['post', 'get'])
@is_user_logged_in
def buy():
    cur = mysql.connection.cursor()
    nat = cur.execute("SELECT * FROM orders WHERE user_name = %s", [session['user_username']])
    if nat > 0:
        form = CartbuyForm(request.form)
        if request.method == 'POST' and form.validate():
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM orders WHERE user_name = %s", [session['user_username']])
            buy_orders = cur.fetchall()
            for order in buy_orders:
                user_id = order['user_id']
                user_name = order['user_name']
                product_id = order['product_id']
                product_name = order['product_name']
                quantity = order['quantity']
                price = order['price']
                discount = order['discount']
                files = order['files']
                cur.execute("INSERT INTO buy_orders(user_id, user_name, status, product_id, product_name,\
                                                                quantity, price, discount, files)\
                                                                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", \
                            (user_id, user_name, 'Pending', product_id, product_name, \
                             quantity, price, discount, files))
                mysql.connection.commit()
            result = cur.execute("SELECT country FROM buy_orders WHERE country = '' AND user_name = %s", [session['user_username']])
            if result > 0:
                country = request.form['country']
                region = request.form['region']
                address = form.address.data
                phone_number = form.phone_number.data
                comments = form.comments.data
                cur.execute("UPDATE buy_orders SET country = %s, region = %s, address = %s, phone_number = %s, comments = %s WHERE  country = '' AND user_name = %s", \
                    [country, region, address, phone_number, comments, session['user_username']])

                cur.execute("SELECT * FROM orders WHERE user_name = %s", [session['user_username']])
                confirm_orders = cur.fetchall()
                for confirm_order in confirm_orders:
                    product_name = confirm_order['product_name']
                    cur.execute("UPDATE products SET number_of_sales = number_of_sales + 1 WHERE product_name = %s", [product_name])
                    mysql.connection.commit()

                for confir_order in confirm_orders:
                    produc_name = confir_order['product_name']
                    cur.execute("UPDATE slider_products SET number_of_sales = number_of_sales + 1 WHERE product_name = %s", [produc_name])
                    mysql.connection.commit()

                cur.execute("DELETE FROM orders WHERE user_name = %s", [session['user_username']])
                mysql.connection.commit()
                cur.close()
                flash('Your order is successfully sent!', 'success')
                return redirect(url_for('home'))
            elif result == 0:
                cur.close()
                flash('you can not be able to buy until you add product to your cart', 'danger')
                return redirect(url_for('add_to_cart'))
        return render_template('buy.html', form=form)
    elif nat == 0:
        flash('you can not be able to buy until you add product to your cart', 'danger')
        return redirect(url_for('add_to_cart'))


# add product to the cart

@app.route('/add_product_to_cart/<id>', methods=['post', 'get'])
@is_user_logged_in
def add_product_to_cart(id):
    cur = mysql.connection.cursor()

    result = cur.execute("SELECT product_name FROM orders WHERE product_id = %s AND user_name = %s ", [id, session['user_username']])
    if result > 0:
        flash('You can not add this product because its already added before!', 'danger')
        return redirect(url_for('add_to_cart'))
    if result == 0:
        cur.execute("SELECT * FROM products WHERE id = %s", [id])
        product = cur.fetchone()
        product_id = product['id']
        product_name = product['product_name']
        product_price = product['price']
        product_discount = product['discount']
        product_files = product['files']
        user_name = session['user_username']
        cur.execute("SELECT id FROM users WHERE username = %s", [session['user_username']])
        res = cur.fetchone()
        user_id = res['id']
        cur.execute("INSERT INTO orders(user_id, user_name, status, product_id, quantity,\
                                     product_name, price, discount, files)\
                                     VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", \
                    (user_id, user_name, 'Pending', product_id, 1, product_name, \
                     product_price, product_discount, product_files))
        mysql.connection.commit()
        cur.close()
        flash('Added successfully to your cart', 'success')
        return redirect(url_for('add_to_cart'))
    return redirect(url_for('home'))


# add product to the cart from slider

@app.route('/add_product_to_cart_from_slider/<id>', methods=['post', 'get'])
@is_user_logged_in
def add_product_to_cart_from_slider(id):
    cur = mysql.connection.cursor()

    proid = (int(id) * int(-1))
    result = cur.execute("SELECT product_name FROM orders WHERE product_id = %s AND user_name = %s ", [proid, session['user_username']])
    if result > 0:
        flash('You can not add this product because its already added before!', 'danger')
        return redirect(url_for('add_to_cart'))
    if result == 0:
        cur.execute("SELECT * FROM slider_products WHERE id = %s", [id])
        product = cur.fetchone()
        # product_id = product['id']
        product_id = (int(product['id']) * int(-1))
        product_name = product['product_name']
        product_price = product['price']
        product_discount = product['discount']
        product_files = product['files']
        user_name = session['user_username']
        cur.execute("SELECT id FROM users WHERE username = %s", [session['user_username']])
        res = cur.fetchone()
        user_id = res['id']
        cur.execute("INSERT INTO orders(user_id, user_name, status, product_id, quantity,\
                                     product_name, price, discount, files)\
                                     VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", \
                    (user_id, user_name, 'Pending', product_id, 1, product_name, \
                     product_price, product_discount, product_files))
        mysql.connection.commit()
        cur.close()
        flash('Added successfully to your cart', 'success')
        return redirect(url_for('add_to_cart'))
    return redirect(url_for('home'))


# increase cart product quantity in cart page

@app.route('/increase_cart_product_quantity/<id>', methods=['post', 'get'])
@is_user_logged_in
def increase_cart_product_quantity(id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE orders SET quantity = quantity + 1 WHERE product_id = {}".format(id))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('add_to_cart'))


# edit cart product quantity in cart page

@app.route('/edit_cart_product_quantity/<id>', methods=['post', 'get'])
@is_user_logged_in
def edit_cart_product_quantity(id):
    quantity = request.form['quantity']
    if int(quantity) >= 1:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE orders SET quantity = %s WHERE product_id = %s", [quantity, id])
        mysql.connection.commit()
        cur.close()
        flash('You have updated the product quantity successfully!', 'success')
    else:
        pass
        flash('You can not put the quantity less than one!', 'danger')
    return redirect(url_for('add_to_cart'))


# decrease cart product quantity in cart page

@app.route('/decrease_cart_product_quantity/<id>', methods=['post', 'get'])
@is_user_logged_in
def decrease_cart_product_quantity(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT quantity FROM orders WHERE product_id = %s", [id])
    cart_product = cur.fetchone()
    product_quantity = cart_product['quantity']
    if product_quantity <= 1:
        flash('You can not put the quantity less than one!', 'danger')
        pass
    if product_quantity > 1:
        cur.execute("UPDATE orders SET quantity = quantity - 1 WHERE product_id = {}".format(id))
        mysql.connection.commit()
    cur.close()
    return redirect(url_for('add_to_cart'))


# delete product from cart page

@app.route('/delete_product_from_cart/<id>', methods=['post', 'get'])
@is_user_logged_in
def delete_product_from_cart(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM orders WHERE product_id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash('You have deleted the product successfully from your cart!', 'success')
    return redirect(url_for('add_to_cart'))


# add product review
@app.route('/product_review/<id>', methods=['post', 'get'])
@is_user_logged_in
def product_review(id):
    cur = mysql.connection.cursor()

    result = cur.execute("SELECT user_name FROM reviews WHERE user_name = %s", [session['user_username']])
    if result == 0:
        cur.execute("SELECT id, product_name FROM products WHERE id = %s", [id])
        product = cur.fetchone()
        product_id = product['id']
        product_name = product['product_name']
        cur.execute("SELECT id, username FROM users WHERE username = %s", [session['user_username']])
        user = cur.fetchone()
        user_id = user['id']
        user_name = user['username']

        product_rate = request.form['rate']
        review = request.form['product_review_area']

        cur.execute("INSERT INTO reviews(user_id, user_name, product_id, product_name, rate, review)\
                     VALUES(%s, %s, %s, %s, %s, %s)", \
                    (user_id, user_name, product_id, product_name, product_rate, review))
        mysql.connection.commit()
        flash('Your review now added successfully!', 'success')
    else:
        flash('You can not add two reviews for one product!', 'danger')
    cur.close()
    return redirect(url_for('home'))


# A common part between the admin and the user ********************************************************


# preview product page

@app.route('/preview_production/<id>/')
def preview_production(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT COUNT(product_id) FROM reviews WHERE product_id={}".format(id))
    reviews = cur.fetchone()
    count_reviews = reviews['COUNT(product_id)']

    reviewresult = cur.execute("SELECT * FROM reviews WHERE product_id={} ORDER BY id DESC limit 1".format(id))
    review = cur.fetchone()

    cur.execute("SELECT * FROM products WHERE id={}".format(id))
    product = cur.fetchone()
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    cur.execute("SELECT * FROM categories")
    categories = cur.fetchall()
    cur.execute("UPDATE products SET number_of_views = number_of_views + 1 WHERE id={}".format(id))
    mysql.connection.commit()

    cur.execute("SELECT SUM(rate) / COUNT(product_name) AS avg_rate FROM reviews WHERE product_id = %s;", [id])
    rate = cur.fetchone()

    cur.close()
    return render_template('preview_production.html', product=product, products=products, categories=categories, count_reviews=count_reviews, review=review, reviewresult=reviewresult, rate=rate)


# preview slider product page

@app.route('/preview_production_slider/<id>/')
def preview_production_slider(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM slider_products WHERE id={}".format(id))
    product = cur.fetchone()
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    cur.execute("SELECT * FROM categories")
    categories = cur.fetchall()
    cur.execute("UPDATE slider_products SET number_of_views = number_of_views + 1 WHERE id={}".format(id))
    mysql.connection.commit()
    cur.close()
    return render_template('preview_production_slider.html', product=product, products=products, categories=categories)


# show all products in specific category 

@app.route('/categories/<category>', methods=['post', 'get'])
def categories(category):
    cur = mysql.connection.cursor()
    cur.execute("SELECT category FROM categories")
    all_categories = cur.fetchall()
    result = cur.execute("SELECT * FROM products WHERE category=%s", [category])
    categories = cur.fetchall()
    cur.close()
    if result > 0:
        return render_template('catigories.html', categories=categories, all_categories=all_categories)
    else:
        msg = 'No Products Found!'
        return render_template('catigories.html', msg=msg, all_categories=all_categories)


# user search bar

@app.route('/user_search', methods=['GET', 'POST'])
def user_search():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM `buy_sell`.`products` \
                             WHERE( CONVERT(`product_name` USING utf8)\
                             LIKE %s)", [["%" + request.form['search'] + "%"]])
        categories = cur.fetchall()
        cur.close()
        if result > 0:
            return render_template('catigories.html', categories=categories)
        else:
            flash('No Products Found', 'warning')
            return redirect(url_for('home'))


# admin part ***********************************************************************************************

# admin login page

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE username = BINARY %s AND permission='admin'", [username])
        if result > 0:
            data = cur.fetchone()
            password = data['password']
            if sha256_crypt.verify(password_candidate, password):
                cur.execute("SELECT files FROM users WHERE username = %s", [username])
                files = cur.fetchone()
                image = files['files']
                session['admin_logged_in'] = True
                session['admin_username'] = username
                session['admin_image'] = image
                cur.close()
                flash('Now You Are Logged In ', 'success')
                return redirect(url_for('admin_dashboard'))
            else:
                error = 'Wrong Password!'
                return render_template('admin_login.html', error=error)
        else:
            error = 'Username Can Not Be Found!'
            return render_template('admin_login.html', error=error)
    return render_template('admin_login.html')


# check if admin is still logged in 

def is_admin_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'admin_logged_in' in session :
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please Login', 'danger')
            return redirect(url_for('admin_login'))
    return wrap


# admin log out

@app.route('/admin/logout')
@is_admin_logged_in
def admin_logout():
    session.clear()
    flash('You Are Now Logged Out', 'success')
    return redirect(url_for('admin_login'))


# admin dashboard page

@app.route('/admin/', methods=['post', 'get'])
@is_admin_logged_in
def admin_dashboard():
    cur = mysql.connection.cursor()
    cur.execute("SELECT COUNT(id) FROM slider_products")
    sliders = cur.fetchone()
    count_sliders = sliders['COUNT(id)']
    cur.execute("SELECT COUNT(id) FROM products")
    products = cur.fetchone()
    count_products = products['COUNT(id)']
    cur.execute("SELECT COUNT(id) FROM users")
    users = cur.fetchone()
    count_users = users['COUNT(id)']
    cur.execute("SELECT COUNT(category) FROM categories")
    categories = cur.fetchone()
    count_categories = categories['COUNT(category)']
    cur.close()
    return render_template('admin_dashboard.html', count_sliders=count_sliders, count_products=count_products, count_users=count_users, count_categories=count_categories, admin_name=session['admin_username'], admin_image=session['admin_image'])


# product validators form

class AddProductForm(Form):
    product_name = StringField('Name Of Product', [validators.InputRequired(), validators.length(min=1, max=180)])
    description = TextAreaField('Description', [validators.InputRequired()])
    price = IntegerField('Price', [validators.InputRequired()])
    discount = StringField('Discount Percentage %')
    # files = FileField('Add picture to Your Product', [validators.InputRequired()])


# admin add new product page

@app.route('/admin/add_product', methods=['post', 'get'])
@is_admin_logged_in
def add_product():
    form = AddProductForm(request.form)
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT category FROM categories")
    categories = cur.fetchall()
    cur.close()
    if result > 0:
        if request.method == 'POST' and form.validate():
            product_name = form.product_name.data

            folder = os.path.exists(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product_name))
            if folder == True:
                flash('Folder Name Already Exists', 'warning')
                return redirect(url_for('add_product'))
            cur = mysql.connection.cursor()
            cur.execute("SELECT product_name FROM products WHERE product_name = %s", [product_name])
            res = cur.fetchone()
            if product_name in str(res):
                msg = "Product Name Already Exists"
                return render_template('admin_add_production.html', form=form, msg=msg, admin_name=session['admin_username'], admin_image=session['admin_image'])

            if request.method == 'POST' and form.validate():
                file = request.files['file']
                if file.filename == '':
                    flash('You Have to Select a File!', 'warning')
                if file and allowed_file(file.filename):
                    try:
                        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product_name))
                        os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product_name))
                    except:
                        os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product_name))
                    filename = secure_filename(file.filename)
                    dir = r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product_name)
                    file.save(os.path.join(dir, filename))
                    category = request.form['categories']
                    description = form.description.data.lower()
                    price = form.price.data
                    discount = form.discount.data

                    if discount != '' and discount != ' ':
                        p = round((float(price) * float(discount)) / 100, 2)
                        cur = mysql.connection.cursor()
                        cur.execute("INSERT INTO products(category, product_name, description, price, discount, files)\
                                                     VALUES(%s, %s, %s, %s, %s, %s)", \
                                    (category, product_name, description, price, p, filename))
                        mysql.connection.commit()
                        cur.close()
                        flash('Your Product is published successfully!', 'success')
                        return redirect(url_for('admin_dashboard'))

                    if discount == "" or discount == " ":
                        p = 0
                        cur = mysql.connection.cursor()
                        cur.execute("INSERT INTO products(category, product_name, description, price, discount, files)\
                                                     VALUES(%s, %s, %s, %s, %s, %s)", \
                                    (category, product_name, description, price, p, filename))
                        mysql.connection.commit()
                        cur.close()
                        flash('Your Product is published successfully!', 'success')
                        return redirect(url_for('admin_dashboard'))

    elif result == 0:
        flash('Create an category first to add a new product', 'warning')
        return redirect(url_for('admin_dashboard'))

    return render_template('admin_add_production.html', form=form, categories=categories, admin_name=session['admin_username'], admin_image=session['admin_image'])
                                
                # cur = mysql.connection.cursor()
                # cur.execute("INSERT INTO products(category, product_name, description, price, discount, files)\
                #              VALUES(%s, %s, %s, %s, %s, %s)", \
                #             (category, product_name, description, price, p, filename))
                # mysql.connection.commit()
                # cur.close()
                # flash('Your Product is published successfully!', 'success')
                # return redirect(url_for('admin_dashboard'))
    # return render_template('admin_add_production.html', form=form, categories=categories)


# admin edit product page

@app.route('/admin/edit_product/<id>', methods=['post', 'get'])
@is_admin_logged_in
def edit_product(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT category FROM categories")
    categories = cur.fetchall()
    cur.close()
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products WHERE id={}".format(id))
    product = cur.fetchone()
    cur.close()
    form = AddProductForm(request.form)
    form.product_name.data = product['product_name']
    form.description.data = product['description']
    form.price.data = product['price']
    # form.discount.data = product['discount']
    
    
    d = round((float(product['discount']) * float(100))/float(form.price.data), 2)
    form.discount.data = d
    
    
    if request.method == 'POST' and form.validate():
        product_name = request.form['product_name']
        file = request.files['file']
        if file and allowed_file(file.filename):
            rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product['product_name']))
            os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product_name))
            filename = secure_filename(file.filename)
            dir = r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product_name)
            file.save(os.path.join(dir, filename))
        
            category = request.form['categories']
            description = request.form['description']
            price = request.form['price']
            discount = request.form['discount']

            if discount == "" or discount == " ":
                p = 0
                cur = mysql.connection.cursor()
                cur.execute("UPDATE products SET category=%s, product_name=%s, description=%s, price=%s,\
                                         discount=%s, files=%s WHERE id=%s", \
                            (category, product_name, description, price, p, filename, id))
                mysql.connection.commit()
                cur.close()
                flash('Your Product Has been Edited successfully!', 'success')
                return redirect(url_for('admin_dashboard'))
            
            p = round((float(price) * float(discount)) / 100, 2)
            
            cur = mysql.connection.cursor()
            cur.execute("UPDATE products SET category=%s, product_name=%s, description=%s, price=%s,\
                         discount=%s, files=%s WHERE id=%s", \
                        (category, product_name, description, price, p, filename, id))
            mysql.connection.commit()
            cur.close()
            flash('Your Product Has been Edited successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
        elif file.filename == '' or 'file' not in request.files:
            os.rename(os.path.join(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product['product_name'])),
                      os.path.join(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product_name)))
            category = request.form['categories']
            description = request.form['description']
            price = request.form['price']
            discount = request.form['discount']

            if discount == "" or discount == " ":
                p = 0
                cur = mysql.connection.cursor()
                cur.execute("UPDATE products SET category=%s, product_name=%s, description=%s, price=%s,\
                                                     discount=%s WHERE id=%s", \
                            (category, product_name, description, price, p, id))
                mysql.connection.commit()
                cur.close()
                flash('Your Product Has been Edited successfully!', 'success')
                return redirect(url_for('admin_dashboard'))
            
            p = round((float(price) * float(discount)) / 100, 2)
            
            cur = mysql.connection.cursor()
            cur.execute("UPDATE products SET category=%s, product_name=%s, description=%s, price=%s,\
                                     discount=%s WHERE id=%s", \
                        (category, product_name, description, price, p, id))
            mysql.connection.commit()
            cur.close()
            flash('Your Product Has been Edited successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
    return render_template('admin_edit_production.html', form=form, categories=categories, admin_name=session['admin_username'], admin_image=session['admin_image'])


# admin delete product

@app.route('/admin/delete_product/<id>', methods=['post', 'get'])
@is_admin_logged_in
def delete_product(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT product_name FROM products WHERE id = %s", [id])
    name = cur.fetchone()
    n = name['product_name']
    try:
        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(n))
    except:
        pass
    cur.execute("DELETE FROM products WHERE id = %s", [id])
    cur.execute("DELETE FROM orders WHERE product_id = %s", [id])
    cur.execute("DELETE FROM reviews WHERE product_id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash('Your Product Has been Deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


# admin delete all products

@app.route('/admin/delete_all_products', methods=['post', 'get'])
@is_admin_logged_in
def delete_all_products():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE products")
    cur.execute("TRUNCATE reviews")
    mysql.connection.commit()
    cur.close()
    try:
        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products")
        flash('You Has been Deleted All Products successfully!', 'success')
    except:
        flash('You Has been Already Deleted All Products successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


# slider product validators form

class AddProductsliderForm(Form):
    product_name = StringField('Name Of Product', [validators.InputRequired(), validators.length(min=1, max=180)])
    description = TextAreaField('Description', [validators.InputRequired()])
    price = IntegerField('Price', [validators.InputRequired()])
    discount = StringField('Discount Percentage %')
    # files = FileField('Add picture to Your Product', [validators.InputRequired()])


# admin add new slider product page

@app.route('/admin/add_product_slider', methods=['post', 'get'])
@is_admin_logged_in
def add_product_slider():
    form = AddProductsliderForm(request.form)
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT category FROM categories")
    categories = cur.fetchall()
    cur.close()
    if result > 0:
        if request.method == 'POST' and form.validate():
            product_name = form.product_name.data

            folder = os.path.exists(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products\{}".format(product_name))
            if folder == True :
                flash('Folder Name Already Exists', 'warning')
                return redirect(url_for('add_product_slider'))
            cur = mysql.connection.cursor()
            cur.execute("SELECT product_name FROM slider_products WHERE product_name = BINARY %s", [product_name])
            res = cur.fetchone()
            if product_name in str(res):
                msg = "Product Name Already Exists"
                return render_template('admin_add_production_slider.html', form=form, msg=msg)
            slider_result = cur.execute("SELECT * FROM slider_products")
            if slider_result < 3:

                file = request.files['file']
                if file.filename == '':
                    flash('You Have to Select a File!', 'warning')
                if file and allowed_file(file.filename):
                    try:
                        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products\{}".format(product_name))
                        os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products\{}".format(product_name))
                    except:
                        os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products\{}".format(product_name))
                    filename = secure_filename(file.filename)
                    dir = r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products\{}".format(product_name)
                    file.save(os.path.join(dir, filename))
                    category = request.form['categories']
                    description = form.description.data.lower()
                    price = form.price.data
                    discount = form.discount.data

                    if discount != '' and discount != ' ':
                        p = round((float(price) * float(discount)) / 100, 2)
                        cur = mysql.connection.cursor()
                        cur.execute("INSERT INTO slider_products(category, product_name, description, price, discount, files)\
                                                     VALUES(%s, %s, %s, %s, %s, %s)", \
                                    (category, product_name, description, price, p, filename))
                        mysql.connection.commit()
                        cur.close()
                        flash('Your Product is published to the slider uccessfully!', 'success')
                        return redirect(url_for('admin_dashboard'))

                    if discount == "" or discount == " ":
                        p = 0
                        cur = mysql.connection.cursor()
                        cur.execute("INSERT INTO slider_products(category, product_name, description, price, discount, files)\
                                                     VALUES(%s, %s, %s, %s, %s, %s)", \
                                    (category, product_name, description, price, p, filename))
                        mysql.connection.commit()
                        cur.close()
                        flash('Your Product is published to the slider successfully!', 'success')
                        return redirect(url_for('admin_dashboard'))
            else:
                flash('You can not add more 3 products in the slider!', 'warning')
                return redirect(url_for('admin_dashboard'))
    elif result == 0:
        flash('Create an category first to add new slider product', 'warning')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_add_production_slider.html', form=form, categories=categories, admin_name=session['admin_username'], admin_image=session['admin_image'])


# admin edit slider product page

@app.route('/admin/edit_product_slider/<id>', methods=['post', 'get'])
@is_admin_logged_in
def edit_product_slider(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT category FROM categories")
    categories = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM slider_products WHERE id={}".format(id))
    product = cur.fetchone()
    cur.close()
    form = AddProductForm(request.form)
    form.product_name.data = product['product_name']
    form.description.data = product['description']
    form.price.data = product['price']
    # form.discount.data = product['discount']

    d = round((float(product['discount']) * float(100)) / float(form.price.data), 2)
    form.discount.data = d

    if request.method == 'POST' and form.validate():
        product_name = request.form['product_name']
        file = request.files['file']
        if file and allowed_file(file.filename):
            rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products\{}".format(product['product_name']))
            os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products\{}".format(product_name))
            filename = secure_filename(file.filename)
            dir = r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products\{}".format(product_name)
            file.save(os.path.join(dir, filename))

            category = request.form['categories']
            description = request.form['description']
            price = request.form['price']
            discount = request.form['discount']

            if discount == "" or discount == " ":
                p = 0
                cur = mysql.connection.cursor()
                cur.execute("UPDATE slider_products SET category=%s, product_name=%s, description=%s, price=%s,\
                                         discount=%s, files=%s WHERE id=%s", \
                            (category, product_name, description, price, p, filename, id))
                mysql.connection.commit()
                cur.close()
                flash('Your slider Product Has been Edited successfully!', 'success')
                return redirect(url_for('admin_dashboard'))
            
            p = round((float(price) * float(discount)) / 100, 2)

            cur = mysql.connection.cursor()
            cur.execute("UPDATE slider_products SET category=%s, product_name=%s, description=%s, price=%s,\
                         discount=%s, files=%s WHERE id=%s", \
                        (category, product_name, description, price, p, filename, id))
            mysql.connection.commit()
            cur.close()
            flash('Your slider Product Has been Edited successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
        elif file.filename == '' or 'file' not in request.files:
            os.rename(os.path.join(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products\{}".format(product['product_name'])),
                      os.path.join(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products\{}".format(product_name)))
            category = request.form['categories']
            description = request.form['description']
            price = request.form['price']
            discount = request.form['discount']

            if discount == "" or discount == " ":
                p = 0
                cur = mysql.connection.cursor()
                cur.execute("UPDATE slider_products SET category=%s, product_name=%s, description=%s, price=%s,\
                                                     discount=%s WHERE id=%s", \
                            (category, product_name, description, price, p, id))
                mysql.connection.commit()
                cur.close()
                flash('Your slider Product Has been Edited successfully!', 'success')
                return redirect(url_for('admin_dashboard'))
            
            p = round((float(price) * float(discount)) / 100, 2)
            
            
            cur = mysql.connection.cursor()
            cur.execute("UPDATE slider_products SET category=%s, product_name=%s, description=%s, price=%s,\
                                     discount=%s WHERE id=%s", \
                        (category, product_name, description, price, p, id))
            mysql.connection.commit()
            cur.close()
            flash('Your slider Product Has been Edited successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
    return render_template('admin_edit_production_slider.html', form=form, categories=categories, admin_name=session['admin_username'], admin_image=session['admin_image'])


# admin delete slider product

@app.route('/admin/delete_product_slider/<id>', methods=['post', 'get'])
@is_admin_logged_in
def delete_product_slider(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT product_name FROM slider_products WHERE id = %s", [id])
    name = cur.fetchone()
    n = name['product_name']
    try:
        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products\{}".format(n))
    except:
        pass
    cur.execute("DELETE FROM slider_products WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash('Your slider Product Has been Deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


# admin delete all slider products

@app.route('/admin/delete_all_slider_products', methods=['post', 'get'])
@is_admin_logged_in
def delete_all_slider_products():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE slider_products")
    mysql.connection.commit()
    cur.close()
    try:
        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products")
        flash('You Has been Deleted All slider Products successfully!', 'success')
    except:
        flash('You Has been Already Deleted All slider Products successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


# admin create user account validator form

class AdduserForm(Form):
    first_name = StringField('First Name', [validators.InputRequired()])
    last_name = StringField('Last Name', [validators.InputRequired()])
    username = StringField('User Name', [validators.InputRequired()])
    password = PasswordField('Password',
                             [validators.DataRequired(), validators.Length(min=6, max=100),
                              validators.EqualTo('confirm', message='Passwords Do Not Match')])
    confirm = PasswordField('Confirm Password', [validators.DataRequired()])


# admin create user account page

@app.route('/admin/add_user', methods=['post', 'get'])
@is_admin_logged_in
def add_user():
    form = AdduserForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data

        folder = os.path.exists(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\{}".format(username))
        if folder == True:
            flash('Folder Name Already Exists', 'warning')
            return redirect(url_for('add_user'))


        cur = mysql.connection.cursor()
        cur.execute("SELECT username FROM users WHERE username = %s", [username])
        res = cur.fetchone()
        if username in str(res):
            msg = "User Name Already Exists"
            return render_template('admin_add_user.html', form=form, msg=msg, admin_name=session['admin_username'], admin_image=session['admin_image'])
        else:
            permission = request.form['permissions']
            first_name = form.first_name.data.lower()
            last_name = form.last_name.data.lower()
            email = request.form['email'].lower()
            gender = request.form['gender']
            country = request.form['country']
            username = form.username.data
            password = sha256_crypt.encrypt(str(form.password.data))
            file = request.files['file']
            if file.filename == '':
                flash('You Have to Select a File!', 'warning')
            try:
                rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\{}".format(username))
                os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\{}".format(username))
            except:
                os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\{}".format(username))
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                dir = r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\{}".format(username)
                file.save(os.path.join(dir, filename))
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO users(permission, first_name, last_name,\
                             email, gender, country, username, password, files)\
                             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", \
                            (permission, first_name, last_name, email, gender,\
                             country, username, password, filename))
                mysql.connection.commit()
                cur.close()
                flash('You Have Created a User Account successfully!', 'success')
                return redirect(url_for('admin_dashboard'))
    return render_template('admin_add_user.html', form=form, admin_name=session['admin_username'], admin_image=session['admin_image'])


# admin delete user 

@app.route('/admin/delete_user/<id>', methods=['post', 'get'])
@is_admin_logged_in
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT username FROM users WHERE id = %s", [id])
    name = cur.fetchone()
    n = name['username']
    try:
        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\{}".format(n))
    except:
        pass
    cur.execute("DELETE FROM users WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash('You Have Deleted User Account successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


# admin add new category validator form

class CategoryForm(Form):
    category = StringField('Category', [validators.InputRequired(), validators.length(min=1, max=100)])
    

# admin add new category page

@app.route('/admin/add_category', methods=['post', 'get'])
@is_admin_logged_in
def add_category():
    form = CategoryForm(request.form)
    if request.method == 'POST' and form.validate():
        category = form.category.data.lower()
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM categories WHERE category = BINARY %s", [category])
        if result > 0:
            flash('This Category Already Exists', 'warning')
            return redirect(url_for('admin_dashboard'))
        if category == ' ':
            flash('You Should Type A Word!', 'warning')
            return redirect(url_for('add_category'))
        if result == 0:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO categories (category) VALUES(%s);", ([category]))
            mysql.connection.commit()
            cur.close()
            flash('You Have Added New Category successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
    return render_template('admin_add_category.html', form=form, admin_name=session['admin_username'], admin_image=session['admin_image'])


# admin edit category page

@app.route('/admin/edit_category/<current_category>', methods=['post', 'get'])
@is_admin_logged_in
def edit_category(current_category):
        cur = mysql.connection.cursor()
        cur.execute("SELECT category FROM categories Where category=%s;", [current_category])
        cat = cur.fetchone()
        cur.close()
        form = CategoryForm(request.form)
        form.category.data = cat['category']
        if request.method == 'POST' and form.validate():
            category = request.form['category'].lower()
            if category == ' ':
                flash('You Should Type A Word!', 'warning')
                return redirect(url_for('add_category'))
            cur = mysql.connection.cursor()
            cur.execute("UPDATE categories SET category=%s WHERE category=%s;", ([category], [current_category]))
            cur.execute("UPDATE products SET category=%s WHERE category=%s", \
                        ([category], [current_category]))
            mysql.connection.commit()
            cur.close()
            flash('You Have Edited Category successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
        return render_template('admin_edit_category.html', form=form, admin_name=session['admin_username'], admin_image=session['admin_image'])


# admin delete category 

@app.route('/admin/delete_category/<category>', methods=['post', 'get'])
@is_admin_logged_in
def delete_category(category):
        cur = mysql.connection.cursor()
        prod = cur.execute("SELECT product_name FROM products WHERE category=%s", [category])
        if prod > 0:
            flash('You Have products in This category', 'success')
            # pass
        products = cur.fetchall()
        for product in products:
            rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product['product_name']))
        slider = cur.execute("SELECT product_name FROM slider_products WHERE category=%s", [category])
        if slider > 0:
            pass
        sliders = cur.fetchall()
        for slider in sliders:
            rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products\{}".format(slider['product_name']))
        cur.execute("DELETE FROM slider_products WHERE category=%s", [category])
        cur.execute("DELETE FROM products WHERE category=%s", [category])
        cur.execute("DELETE FROM categories Where category=%s;", [category])
        mysql.connection.commit()
        cur.close()        
        flash("You Have Deleted Category With it's products Successfully!", 'success')
        return redirect(url_for('admin_dashboard'))


# admin delete all categories

@app.route('/admin/delete_all_categories', methods=['post', 'get'])
@is_admin_logged_in
def delete_all_categories():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE categories")
    cur.execute("TRUNCATE products")
    cur.execute("TRUNCATE slider_products")
    cur.execute("TRUNCATE orders")
    cur.execute("TRUNCATE buy_orders")
    cur.execute("TRUNCATE reviews")
    mysql.connection.commit()
    cur.close()
    try:
        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products")
        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products")
        flash('You Has been Deleted All Categories and Products Successfully!', 'success')
    except:
        flash('You Has been Deleted All Categories and Products Successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


# admin delete all users

@app.route('/admin/delete_all_users', methods=['post', 'get'])
@is_admin_logged_in
def delete_all_users():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT username FROM users WHERE permission = 'user'")
    if result >0:
        name = cur.fetchall()
        for n in name:
            rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\{}".format(n['username']))
    elif result == 0:
        pass
    cur.execute("DELETE FROM users WHERE permission = 'user' ")
    mysql.connection.commit()
    cur.close()
    flash('You Have Deleted All Users Account with their files successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


# admin delete all accounts

@app.route('/admin/delete_all_accounts', methods=['post', 'get'])
@is_admin_logged_in
def delete_all_accounts():
    try:
        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users")
        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products")
        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products")
    except:
        pass
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE users")
    cur.execute("TRUNCATE categories")
    cur.execute("TRUNCATE products")
    cur.execute("TRUNCATE slider_products")
    cur.execute("TRUNCATE orders")
    cur.execute("TRUNCATE buy_orders")
    cur.execute("TRUNCATE reviews")
    mysql.connection.commit()
    cur.close()
    session.clear()
    flash('You Have Deleted All Accounts with their files successfully!', 'success')
    return redirect(url_for('admin_login'))


# admin accept orders

@app.route('/admin/accept_orders/<id>', methods=['post', 'get'])
@is_admin_logged_in
def accept_orders(id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE buy_orders SET status = %s WHERE id = %s", (['Accepted'], id))
    mysql.connection.commit()
    cur.close()
    flash('You have accepted the order Successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


# admin accept all orders

@app.route('/admin/accept_all_orders', methods=['post', 'get'])
@is_admin_logged_in
def accept_all_orders():
    cur = mysql.connection.cursor()
    cur.execute("UPDATE buy_orders SET status = %s", (['Accepted']))
    mysql.connection.commit()
    cur.close()
    flash('You have accepted all orders Successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


# admin reject orders

@app.route('/admin/reject_orders/<id>', methods=['post', 'get'])
@is_admin_logged_in
def reject_orders(id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE buy_orders SET status = %s WHERE id = %s", (['Rejected'], id))
    mysql.connection.commit()
    cur.close()
    flash('You have rejected the order Successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


# admin reject all orders

@app.route('/admin/reject_all_orders', methods=['post', 'get'])
@is_admin_logged_in
def reject_all_orders():
    cur = mysql.connection.cursor()
    cur.execute("UPDATE buy_orders SET status = %s", (['Rejected']))
    mysql.connection.commit()
    cur.close()
    flash('You have rejected all orders Successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


# admin search bar

@app.route('/search', methods=['GET', 'POST'])
@is_admin_logged_in
def search():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM `buy_sell`.`products` \
                             WHERE( CONVERT(`product_name` USING utf8)\
                             LIKE %s)", [["%" + request.form['search'] + "%"]])
        categories = cur.fetchall()
        cur.close()
        if result > 0:
            return render_template('catigories.html', categories=categories)
        else:
            flash('No Products Found', 'warning')
            return redirect(url_for('admin_dashboard'))


# admin preview all slider products table page

@app.route('/admin/slider_products_table')
@is_admin_logged_in
def slider_products_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM slider_products")
    slider_products = cur.fetchall()
    cur.execute("SELECT COUNT(id) FROM slider_products")
    sliders = cur.fetchone()
    count_sliders = sliders['COUNT(id)']
    cur.close()
    return render_template('admin_slider_products_table .html', slider_products=slider_products, count_sliders=count_sliders, admin_name=session['admin_username'], admin_image=session['admin_image'])


# admin preview all products table page

@app.route('/admin/products_table')
@is_admin_logged_in
def products_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    cur.close()
    return render_template('admin_products_table.html', products=products, admin_name=session['admin_username'], admin_image=session['admin_image'])


# admin preview all categories table page

@app.route('/admin/categories_table')
@is_admin_logged_in
def categories_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT category FROM categories")
    categories = cur.fetchall()
    for category in categories:
        cc = category['category']
        cur.execute("SELECT COUNT(product_name) FROM products WHERE category = %s", [cc])
        pro_category = cur.fetchone()
        cat = pro_category['COUNT(product_name)']




    cur.execute("SELECT COUNT(category) FROM categories")
    category = cur.fetchone()
    count_categories = category['COUNT(category)']
    cur.execute("SELECT COUNT(id) FROM products")
    products = cur.fetchone()
    count_products = products['COUNT(id)']
    cur.close()
    return render_template('admin_categories_table.html', categories=categories, count_products=count_products, count_categories=count_categories, admin_name=session['admin_username'], admin_image=session['admin_image'])


# admin preview all users table page

@app.route('/admin/users_table')
@is_admin_logged_in
def users_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.execute("SELECT COUNT(username) FROM users WHERE permission = 'user'")
    count_userss = cur.fetchone()
    count_users = count_userss['COUNT(username)']
    cur.close()
    return render_template('admin_users_table.html', users=users, count_users=count_users, admin_name=session['admin_username'], admin_image=session['admin_image'])


# admin preview all users table page

@app.route('/admin/orders_table')
@is_admin_logged_in
def orders_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM buy_orders")
    orders = cur.fetchall()
    cur.close()
    return render_template('admin_orders_table.html', orders=orders, admin_name=session['admin_username'], admin_image=session['admin_image'])


# run whole application function

if __name__ == '__main__':
    app.secret_key = 'osama_blog'
    app.run(debug=True)
