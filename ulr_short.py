from flask import Flask, render_template, request, url_for, redirect, send_from_directory
from flask_mysqldb import MySQL
import MySQLdb
import os
import uuid

database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
# cursor.execute("DROP DATABASE IF EXISTS short;")
cursor.execute("CREATE DATABASE IF NOT EXISTS short DEFAULT CHARSET UTF8")
database.select_db('short')
# cursor.execute("DROP TABLE IF EXISTS short_link;")
cursor.execute("CREATE TABLE IF NOT EXISTS short_link(\
                id INT(11) AUTO_INCREMENT PRIMARY KEY,\
                original_link varchar(255) UNIQUE NOT NULL,\
                short_link TEXT NOT NULL,\
                process_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP );")
database.close()

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'short'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'g.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    cur = mysql.connection.cursor()
    r = request.form['url']
    cur.execute("SELECT original_link FROM short_link WHERE original_link=%s", [r])
    sl = cur.fetchone()
    if r in str(sl):
        cur.execute("SELECT * FROM short_link WHERE original_link=%s", [r])
        sl2 = cur.fetchone()
        return render_template('already_exists.html', sl2=sl2)
    else :
        def random_string(string_length=5):
            return str(uuid.uuid4())[0:string_length]
        cur.execute("INSERT INTO short_link(original_link, short_link)\
                             VALUES(%s, %s)", ([r], ["https://go.gl/" + random_string()]))
        mysql.connection.commit()
        res = cur.execute("SELECT * FROM short_link WHERE original_link=%s", [r])
        short_link = cur.fetchone()
        if res > 0:
            return render_template('result.html', short_link=short_link)
        else:
            msg = 'No Urls Found!'
            return render_template('fail.html', msg=msg, short_link=short_link)
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'osama_blog'
    app.run(debug=True)