from flask_mysqldb import MySQL
from flask import Flask, jsonify
import requests
import MySQLdb

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'facebook_api'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
# cursor.execute("DROP DATABASE IF EXISTS facebook_api;")
cursor.execute("CREATE DATABASE IF NOT EXISTS facebook_api DEFAULT CHARSET UTF8")
database.select_db('facebook_api')
cursor.execute("CREATE TABLE IF NOT EXISTS users(\
                id INT(11) AUTO_INCREMENT PRIMARY KEY,\
                user_id TEXT NOT NULL,\
                posts_id TEXT NOT NULL,\
                story TEXT NOT NULL,\
                created_time VARCHAR(100) NOT NULL,\
                update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP );")
database.close()


@app.route('/<int:id>')
@app.route('/<int:id>/<local>')
def users(id, local=None):
    url = "https://graph.facebook.com/v2.12/{}/posts?access_token=EAACEdEose0cBAFXuepVNHkSY0avpWECwPX5ZBBcGlZCzHi6YRlfred2rseY6Egk5m5X66JMC4ZCo4AhCADYmhKbKXQ0ZA7nHWybsivcDx4aDyl2QZCCPO0rtBD3PmWLqOzgDqmDDRiR1bj1awT3vA4YXUoHLKPlHVbk2ZCwZAk67S94jkgRdZAE6ZB0FmqsOZAvvcZD".format(id)
    result = requests.get(url).json()
    if not local:
        cur = mysql.connection.cursor()
        for res in result['data']:
            try:
                cur.execute("INSERT INTO users(user_id, posts_id, story, created_time) VALUES(%s, %s, %s, %s)",
                            (id, res['id'], res['story'], res['created_time']))
            except:
                pass
        mysql.connection.commit()
        cur.close()
    if local:
        cur = mysql.connection.cursor()
        cur.execute("SELECT posts_id, story, created_time FROM users WHERE user_id = {};".format(id))
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
