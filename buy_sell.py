# some imports
from flask import Flask, render_template, flash, redirect, url_for, session, request, send_from_directory
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, validators, FileField, IntegerField, PasswordField
from passlib.hash import sha256_crypt
from werkzeug.utils import secure_filename
from shutil import rmtree, copyfile, copy2, copy, copyfileobj
from functools import wraps
import MySQLdb
import os


# connect to database in localhost to create database and their tables

database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
# cursor.execute("DROP DATABASE IF EXISTS buy_sell;")
cursor.execute("CREATE DATABASE IF NOT EXISTS buy_sell DEFAULT CHARSET UTF8")
database.select_db('buy_sell')
# cursor.execute("DROP TABLE IF EXISTS users;")
# cursor.execute("DROP TABLE IF EXISTS products;")
# cursor.execute("DROP TABLE IF EXISTS slider_products;")


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
                product_name VARCHAR(255) NOT NULL,\
                description TEXT NOT NULL,\
                price INT(10) NOT NULL,\
                discount FLOAT NOT NULL,\
                files TEXT NOT NULL,\
                create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")

cursor.execute("CREATE TABLE IF NOT EXISTS categories (category VARCHAR(255) PRIMARY KEY);")


# create default admin account if not exists

# try:
#     rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\admin")
#     os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\admin")
#     copyfileobj(r'C:\Users\OSAMA\Desktop\buy_sell\static\admin.png', r'C:\Users\OSAMA\Desktop\buy_sell\static\uploads\users\admin\admin.png')
# except:
#     pass

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
    # cur.execute("SELECT * FROM products WHERE category = %s ORDER BY id DESC  LIMIT 8;", ['hosting'])
    # latest_productss = cur.fetchall()
    cur.close()
    return render_template('home.html', latest_products=latest_products, categories=categories, slider_products_first=slider_products_first, slider_products_second=slider_products_second, slider_products_third=slider_products_third)


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
                cur.close()
                flash('Now You Are Logged In ', 'success')
                return redirect(url_for('home'))
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

@app.route('/logout')
@is_user_logged_in
def user_logout():
    session.clear()
    flash('You Are Now Logged Out', 'success')
    return redirect(url_for('user_login'))


# A common part between the admin and the user ********************************************************


# preview product page

@app.route('/preview_production/<id>/')
def preview_production(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products WHERE id={}".format(id))
    product = cur.fetchone()
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    cur.execute("SELECT * FROM categories")
    categories = cur.fetchall()
    cur.close()
    return render_template('preview_production.html', product=product, products=products, categories=categories)


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
                print(image)
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
        cur.execute("SELECT * FROM categories WHERE category = BINARY %s", [category])
        res = cur.fetchone()
        if category in str(res):
            flash('This Category Already Exists', 'warning')
            return redirect(url_for('admin_dashboard'))
        if category == ' ':
            flash('You Should Type A Word!', 'warning')
            return redirect(url_for('add_category'))
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
    mysql.connection.commit()
    cur.close()
    try:
        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products")
        rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\slider_products")
        flash('You Has been Deleted All Categories and Products Successfully!', 'success')
    except:
        flash('You Has been Deleted All Categories and Products Successfully!', 'success')
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

        #
        # cur.execute("SELECT COUNT(product_name) FROM products WHERE category=%s", [cc])
        # count_products_by_category = cur.fetchall()
        # for products_by_category in count_products_by_category:
        #     print(products_by_category['COUNT(product_name)'])
        #     session['cat'] = products_by_category['COUNT(product_name)']
        #     print(session['cat'])


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
    cur.close()
    return render_template('admin_users_table.html', users=users, admin_name=session['admin_username'], admin_image=session['admin_image'])


# run whole application function

if __name__ == '__main__':
    app.secret_key = 'osama_blog'
    app.run(debug=True)
