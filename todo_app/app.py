from flask import Flask, redirect, url_for,  render_template
from todo_app.data import session_items
from todo_app.flask_config import Config
from flask import request

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/index')
def index():
    list = session_items.get_items()
    return  render_template('index.html', list=list)

@app.route('/hello/<name>')
def hello(name):
   return 'welcome %s' % name

@app.route('/addNewTitle',methods = ['POST'])
def addTitle():
   todo = request.form.get('nm')
   print(todo)
   session_items.add_item(todo)
   # return session_items.add_item(todo)
   return redirect(url_for('index'))  

app.run()