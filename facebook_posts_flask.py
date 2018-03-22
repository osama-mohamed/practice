from flask_mysqldb import MySQL
from flask import Flask, jsonify
import requests
import MySQLdb

dbhost = 'localhost'
dbusername = 'root'
dbpassword = ''
dbname = 'facebook_api'


app = Flask(__name__)
app.config['MYSQL_HOST'] = dbhost
app.config['MYSQL_USER'] = dbusername
app.config['MYSQL_PASSWORD'] = dbpassword
app.config['MYSQL_DB'] = dbname
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


database = MySQLdb.connect(dbhost, dbusername, dbpassword)
cursor = database.cursor()
# cursor.execute("DROP DATABASE IF EXISTS facebook_api;")
cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARSET UTF8".format(dbname))
database.select_db('{}'.format(dbname))
cursor.execute("CREATE TABLE IF NOT EXISTS users(\
                id INT(11) AUTO_INCREMENT PRIMARY KEY,\
                user_id TEXT NOT NULL,\
                posts_id TEXT NOT NULL,\
                story TEXT NOT NULL,\
                message TEXT NOT NULL,\
                created_time VARCHAR(100) NOT NULL,\
                update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP );")
database.close()


@app.route('/users/<int:id>/posts')
@app.route('/users/<int:id>/posts/<local>')
def users(id, local=None):
    token = 'EAACEdEose0cBAItHTDg4ZAnNqLUKrSUWMV5FY3wgToRMHqHxIZBtsoyDVJJCv3D1UivTAk9w0WsjkTzKN1jIJ0Mld0rJUh1wkMMQNjIF0qmA8dZClXG22sMrnNEbEQMdv2Q1Fka6FCUS0ueert2MJaYLx1jR1MkchrXSpPmSTYrXpefJsEeignysvQypN0EcwWTzWvyOepLeaZAYStYC'
    url = "https://graph.facebook.com/v2.12/{}/posts?limit=25&access_token={}".format(id, token)
    result = requests.get(url).json()
    print(result)
    if not local:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM users WHERE user_id = {}".format(id))
        mysql.connection.commit()
        for res in result['data']:
            try:
                cur.execute("INSERT INTO users(user_id, posts_id, story, message, created_time) VALUES(%s, %s, %s, %s, %s)",
                            (id, res['id'], res['story'], '', res['created_time']))
            except:
                cur.execute("INSERT INTO users(user_id, posts_id, story, message, created_time) VALUES(%s, %s, %s, %s, %s)",
                            (id, res['id'], '', res['message'], res['created_time']))
        mysql.connection.commit()
        cur.close()
    if local:
        cur = mysql.connection.cursor()
        cur.execute("SELECT posts_id, story, message, created_time FROM users WHERE user_id = {};".format(id))
        allresult = cur.fetchall()
        cur.close()
        output = []
        for res in allresult:
            output.append({"created_time": res['created_time'],
                           "id": res['posts_id'],
                           "story": res['story']
                           })
        result = {'data': output}
    return jsonify({'message': result})


if __name__ == '__main__':
    app.run(debug=True)
