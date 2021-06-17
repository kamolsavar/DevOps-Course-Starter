import os
from flask import Flask, redirect, url_for,  render_template
from todo_app.data import session_items
from todo_app.flask_config import Config
from flask import request
import requests

app = Flask(__name__)
app.config.from_object(Config)   

KEY=os.getenv("KEY")
TOKEN=os.getenv("TOKEN")

BOARD_ID=os.getenv("BOARD_ID")
ID_LIST_TODO=os.getenv("ID_LIST_TODO")
ID_LIST_DOING=os.getenv("ID_LIST_DOING")
ID_LIST_DONE=os.getenv("ID_LIST_DONE")


class Item:
   
   def __init__(self, id, title, status):
      self.title = title
      self.status = status
      self.id = id

@app.route("/card/<name>/<status>")
def createCard(name, status):
   # todo = request.form.get('nm')
   
   if status == "ToDo":
      idList = ID_LIST_TODO
   elif status == "Doing":
      idList = ID_LIST_DOING
   else:
         idList = ID_LIST_DONE
   r= requests.post('https://api.trello.com/1/cards',  params={'key': KEY, 'token': TOKEN, 'idList' : idList, 'name' : name})
   response = r.json()
   return redirect(url_for('index'))  

@app.route('/index')
def index():
    list = getAllToDoFromTrello()
    return  render_template('index.html', list=list)

def getAllToDoFromTrello():
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
 
@app.route('/addNewTitle',methods = ['POST'])
def addTitle():
   todo = request.form.get('nm')
   print(todo)
   idList = ID_LIST_TODO
   r= requests.post('https://api.trello.com/1/cards',  params={'key': KEY, 'token': TOKEN, 'idList' : idList, 'name' : todo})
   response = r.json()
   return redirect(url_for('index'))  

@app.route('/updateCard/<cardId>/<status>')
def updateCard(cardId, status):
   if status == "ToDo":
      idList = ID_LIST_TODO
   elif status == "Doing":
      idList = ID_LIST_DOING
   else: 
      idList = ID_LIST_DONE
   r= requests.put(f'https://api.trello.com/1/cards/{cardId}',  params={'key': KEY, 'token': TOKEN, 'idList': idList})
   response = r.json()
   return redirect(url_for('index')) 

app.run()
