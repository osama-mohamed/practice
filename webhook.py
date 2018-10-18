from flask import Flask, jsonify, request
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv("USER")
app.config['MAIL_PASSWORD'] = os.getenv("PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods=['POST'])
def index():
  if len(request.json['commits']) > 0:
    output = """
      <h3>Repository {name} Notification Detail</h3>
      <br>
      <ul>
      <li><strong>Repository ID:</strong> {id}</li>
      <br>
      <li><strong>Repository Name:</strong> {name}</li>
      <br>
      <li><strong>Repository Full Name:</strong> {full_name}</li>
      <br>
      <li><strong>Repository URL:</strong> {html_url}</li>
      <br>
      <li><strong>Commit id:</strong> {commit_id}</li>
      <br>
      <li><strong>Commit Message:</strong> {commit_message}</li>
      <br>
      <li><strong>Committed At:</strong> {commit_timestamp}</li>
      <br>
      <li><strong>Commit URL:</strong> {commit_url}</li>
      <br>
      <li><strong>Commit Differences:</strong> {commit_compare}</li>
      <br>
      <li><strong>Commit Author:</strong> {commit_author_name}</li>
      <br>
      <li><strong>Commit Author E-mail:</strong> {commit_author_email}</li>
      <br>
      <li><strong>Commit Author Username:</strong> {commit_author_username}</li>
      <br>
      <hr>
      <br>
      <li style="color: green;"><strong>Added files In Commit:</strong> {commit_added_files}</li>
      <br>
      <li style="color: orange;"><strong>Modified files In Commit:</strong> {commit_modified_files}</li>
      <br>
      <li style="color: red;"><strong>Removed files In Commit:</strong> {commit_removed_files}</li>
      <br>
      <hr>
      </ul>
      <ul>""".format(
      name=request.json['repository']['name'],
      id=request.json['repository']['id'],
      full_name=request.json['repository']['full_name'],
      html_url=request.json['repository']['owner']['html_url'],
      commit_id=request.json['commits'][0]['id'],
      commit_message=request.json['commits'][0]['message'],
      commit_timestamp=request.json['commits'][0]['timestamp'],
      commit_url=request.json['commits'][0]['url'],
      commit_compare=request.json['compare'],
      commit_author_name=request.json['commits'][0]['author']['name'],
      commit_author_email=request.json['commits'][0]['author']['email'],
      commit_author_username=request.json['commits'][0]['author']['username'],
      commit_added_files=request.json['commits'][0]['added'],
      commit_modified_files=request.json['commits'][0]['modified'],
      commit_removed_files=request.json['commits'][0]['removed']
    )
    for x in range(0, len(request.json['commits'][0]['added']) ):
      output += """<br><li style='color: green;'><strong>Added file {index} 
      In Commit:</strong> {file}</li>""".format(index=x + 1, file=request.json['commits'][0]['added'][x])

    for y in range(0, len(request.json['commits'][0]['modified']) ):
      output += """<br><li style='color: orange;'><strong>Modified file {index} 
      In Commit:</strong> {file}</li>""".format(index=y + 1, file=request.json['commits'][0]['modified'][y])

    for z in range(0, len(request.json['commits'][0]['removed']) ):
      output += """<br><li style='color: red;'><strong>Removed file {index} 
      In Commit:</strong> {file}</li>""".format(index=z + 1, file=request.json['commits'][0]['modified'][z])
    output += '</ul>'
    msg = Message(
      request.json['repository']['name'], 
      sender = "Notification from {} {}".format(request.json['repository']['name'], os.getenv("USER")), 
      recipients = [os.getenv("USERTO")]
    )
    msg.body = output
    msg.html = output
    mail.send(msg)
    return jsonify({"done": True})
  else :
    return jsonify({"done": False})



if __name__ == '__main__':
    app.secret_key = 'secret1234'
    app.run()
