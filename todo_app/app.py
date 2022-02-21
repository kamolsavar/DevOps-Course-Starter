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

def create_app():
   app = Flask(__name__)
   app.config.from_object(Config())   

   KEY=os.getenv("KEY")
   TOKEN=os.getenv("TOKEN")

   BOARD_ID=os.getenv("BOARD_ID")
   ID_LIST_TODO=os.getenv("ID_LIST_TODO")
   ID_LIST_DOING=os.getenv("ID_LIST_DOING")
   ID_LIST_DONE=os.getenv("ID_LIST_DONE")

   client = pymongo.MongoClient(os.getenv("MONGO_DB_CONNECTION"), tlsCAFile=certifi.where())
   db = client['test-database'] 
   collection = db.test_collection



   @app.route('/')
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
      todo = request.form.get('nm')
      print(todo)
      collection.insert_one({"Name": todo, "Status": "To Do" })
      return redirect(url_for('index'))  

   @app.route('/updateCard/<cardId>/<status>')
   def updateCard(cardId, status):
      collection.update_one({"_id" : ObjectId(cardId)}, {"$set" : {"Status" : status}})
      print (f"The status :{cardId}")
      return redirect(url_for('index')) 
      
   def get_all_todo_from_trello():
      list= []
      trelloList= requests.get(f'https://api.trello.com/1/boards/{BOARD_ID}/cards', params={'key': KEY, 'token': TOKEN}).json()
      for card in trelloList:
         if card ["idList"] == ID_LIST_TODO:
            status = "ToDo"
         elif card ["idList"]== ID_LIST_DOING:
            status = 'Doing'   
         else:
            status = "Done"
         # list.append({"status":status, "id":card["id"], "title":card["name"]})
         list.append(Item(card["id"], card["name"], status))
      return list  
   
   return app


