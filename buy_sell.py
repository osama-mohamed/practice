from flask import Flask, render_template, flash, redirect, url_for, session, request, send_from_directory
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, validators, FileField, IntegerField
from werkzeug.utils import secure_filename
from shutil import rmtree
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


cursor.execute("CREATE TABLE IF NOT EXISTS users(\
                id INT(11) AUTO_INCREMENT PRIMARY KEY,\
                permission VARCHAR(10) NOT NULL,\
                first_name VARCHAR(100) NOT NULL,\
                last_name VARCHAR(100) NOT NULL,\
                email VARCHAR(100) NOT NULL,\
                sex VARCHAR(10) NOT NULL,\
                country VARCHAR(50) NOT NULL,\
                username VARCHAR(100) NOT NULL,\
                password VARCHAR(100) NOT NULL,\
                files TEXT NOT NULL,\
                register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP );")

cursor.execute("CREATE TABLE IF NOT EXISTS products(\
                id INT(11) AUTO_INCREMENT PRIMARY KEY,\
                category VARCHAR(100) NOT NULL,\
                product_name VARCHAR(255) NOT NULL,\
                description TEXT NOT NULL,\
                price INT(10) NOT NULL,\
                discount INT(10) NOT NULL,\
                files TEXT NOT NULL,\
                create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")


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


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/admin/register')
def admin_register():
    return render_template('register.html')


# home page

@app.route('/admin/')
def admin_dashboard():
    return render_template('index.html')


@app.route('/admin/login')
def admin_login():
    return render_template('login.html')


@app.route('/preview_production/<id>/')
def preview_production(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products WHERE id={}".format(id))
    product = cur.fetchone()
    cur.close()
    return render_template('preview_production.html', product=product)



class AddProductForm(Form):
    product_name = StringField('Name Of Product', [validators.InputRequired()])
    description = TextAreaField('Description', [validators.InputRequired()])
    price = IntegerField('Price', [validators.InputRequired()])
    discount = StringField('Discount')
    # files = FileField('Add picture to Your Product', [validators.InputRequired()])
    
    
@app.route('/admin/add_product', methods=['post', 'get'])
def add_product():
    form = AddProductForm(request.form)
    if request.method == 'POST' and form.validate():
        product_name = form.product_name.data

        cur = mysql.connection.cursor()
        cur.execute("SELECT product_name FROM products WHERE product_name = BINARY %s", [product_name])
        res = cur.fetchone()
        if product_name in str(res):
            msg = "Product Name Already Exists"
            return render_template('admin_add_production.html', form=form, msg=msg)
        else:
            
            file = request.files['file']
            if file.filename == '':
                flash('You Have to Select a File!', 'warning')
            try:
                rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product_name))
                os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product_name))
            except:
                os.makedirs(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product_name))
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                dir = r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(product_name)
                file.save(os.path.join(dir, filename))
                category = request.form['categories']
                description = form.description.data
                price = form.price.data
                discount = form.discount.data
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO products(category, product_name, description, price, discount, files)\
                             VALUES(%s, %s, %s, %s, %s, %s)", \
                             (category, product_name, description, price, discount, filename))
                mysql.connection.commit()
                cur.close()
                flash('Your Product is published successfully!', 'success')
                return redirect(url_for('admin_dashboard'))
    return render_template('admin_add_production.html', form=form)


@app.route('/admin/edit_product/<id>', methods=['post', 'get'])
def edit_product(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products WHERE id={}".format(id))
    product = cur.fetchone()
    cur.close()
    form = AddProductForm(request.form)
    form.product_name.data = product['product_name']
    form.description.data = product['description']
    form.price.data = product['price']
    form.discount.data = product['discount']
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
            cur = mysql.connection.cursor()
            cur.execute("UPDATE products SET category=%s, product_name=%s, description=%s, price=%s,\
                         discount=%s, files=%s WHERE id=%s", \
                        (category, product_name, description, price, discount, filename, id))
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
            cur = mysql.connection.cursor()
            cur.execute("UPDATE products SET category=%s, product_name=%s, description=%s, price=%s,\
                                     discount=%s WHERE id=%s", \
                        (category, product_name, description, price, discount, id))
            mysql.connection.commit()
            cur.close()
            flash('Your Product Has been Edited successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
    return render_template('admin_edit_production.html', form=form)


@app.route('/admin/delete_product/<id>', methods=['post', 'get'])
def delete_product(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT product_name FROM products WHERE id = %s", [id])
    name = cur.fetchone()
    n = name['product_name']
    rmtree(r"C:\Users\OSAMA\Desktop\buy_sell\static\uploads\products\{}".format(n))
    cur.execute("DELETE FROM products WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash('Your Product Has been Deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/products_table')
def products_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return render_template('tables.html', products=products, users=users)



@app.route('/admin/users_table')
def users_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return render_template('users_table.html', users=users)




#cur = mysql.connection.cursor()
#cur.execute("UPDATE users SET files='' WHERE username=%s", [session['username']])
#mysql.connection.commit()
#cur.close()

# run whole application function


if __name__ == '__main__' :
    app.secret_key = 'osama_blog'
    app.run(debug=True)