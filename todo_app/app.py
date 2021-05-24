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

@app.route('/addNewTitle',methods = ['POST', 'GET'])
def addTitle():
   if request.method == 'POST':
      todo = request.form.get('nm')
      print(todo)
      # session_items.add_item(user)
      return session_items.add_item(todo)
      # return redirect(url_for('index'))   
   else:
     todo = request.args.get('nm')
     return redirect(url_for('hello',name = todo))   

app.run()