from email.headerregistry import ContentTypeHeader
import os
import certifi
from bson import ObjectId
import pymongo
from todo_app.item import Item
from flask import Flask, redirect, url_for,  render_template
from todo_app.data import session_items
from todo_app.flask_config import Config
from flask import request
import requests
from todo_app.view_model import ViewModel 
from flask_login import current_user, login_user, logout_user, LoginManager, login_required, UserMixin
from oauthlib.oauth2 import WebApplicationClient  
from todo_app.user import  User

def create_app():
   app = Flask(__name__)
   app.config.from_object(Config())
   app.config['LOGIN_DISABLED'] = os.getenv('LOGIN_DISABLED') == 'True'
   client = pymongo.MongoClient(os.getenv("MONGO_DB_CONNECTION"), tlsCAFile=certifi.where())
   db = client[os.getenv("DATABASE_NAME")] 
   collection = db.test_collection

   login_manager = LoginManager()
   
   @login_manager.unauthorized_handler
   def unauthenticated():
      return redirect('https://github.com/login/oauth/authorize?client_id=' + os.getenv("CLIENT_ID"))  
   
   @login_manager.user_loader
   def load_user(user_id):
      return User(user_id)
 
   login_manager.init_app(app)

   @app.route('/login/callback')
   def log_in_call_back():
      response = requests.post('https://github.com/login/oauth/access_token', headers = {"Accept":"application/json"}, params={"client_id":os.getenv("CLIENT_ID"), "client_secret":os.getenv("CLIENT_SECRET"), "code": request.args.get("code")})
      access_token = response.json()["access_token"]
      response_user_data = requests.get('https://api.github.com/user', headers = {"Authorization" : f"Bearer {access_token}"}) 
      user_id =  response_user_data.json()["id"]
      user = User(user_id)
      login_user(user)
      return redirect(url_for('index')) 
  

   @app.route('/')
   @login_required
   def index():
      json_record_for_todos = collection.find()
      list= []
      for card in json_record_for_todos:
         status = card ["Status"]
         print (f"The Status: {status}")
         print (f"The cardId :{card['_id']}")
         list.append(Item(card["_id"], card["Name"], status))
      print (f"The record is {json_record_for_todos}" )
      view_model = ViewModel(list)
      return  render_template('index.html', view_model=view_model)

   @app.route('/addNewTitle',methods = ['POST'])
   def addTitle():
      if (current_user.role == "Writer"):
         todo = request.form.get('nm')
         print(todo)
         collection.insert_one({"Name": todo, "Status": "To Do" })
         return redirect(url_for('index'))
      else:
         return  "Permission denied", 401     

   @app.route('/updateCard/<cardId>/<status>')
   def updateCard(cardId, status):
      if (current_user.role == "Writer"):
         collection.update_one({"_id" : ObjectId(cardId)}, {"$set" : {"Status" : status}})
         print (f"The status :{cardId}")
         return redirect(url_for('index'))
      else:
         return  "Permission denied", 401      
   
   return app


