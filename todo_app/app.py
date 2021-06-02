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
    

class TransportAPI:
    def __init__(self):
        api_keys = get_application_keys()
        self.payload = api_keys


@app.route('/index')
def index():
    list = getAllToDoFromTrell0()
    return  render_template('index.html', list=list)

def getAllToDoFromTrell0():
   id = '60af9248e87283184d346aa8'
   list= []
   trelloList= requests.get(f'https://api.trello.com/1/boards/{id}/cards', params={'key': KEY, 'token': TOKEN}).json()
   for card in trelloList:
      if card ["idList"] =="60af9248e87283184d346aa9":
         status = "To Do"
      elif card ["idList"]=="60af9248e87283184d346aaa":
         status = 'Doing'   
      else:
         status = "Done"
      list.append({"status":status, "id":card["id"], "title":card["name"]})
   return list  

def createBoard():
   name='ToDoList'
   r= requests.post('https://api.trello.com/1/boards', params={'key': KEY, 'token': TOKEN, 'name': name})
   response=r.json()
   return response  

def getBoard():
   id = '60af9248e87283184d346aa8'
   r= requests.get(f'https://api.trello.com/1/boards/{id}', params={'key': KEY, 'token': TOKEN})
   response=r.json()
   return response     


def createCardList():
   name='Monday'
   boardId= '60af9248e87283184d346aa8'
   r= requests.post(f'https://api.trello.com/1/boards/{boardId}/lists',  params={'key': KEY, 'token': TOKEN, 'name': name})
   response=r.json()
   return response  

@app.route('/createCard')
def createCard():
   idList = '60af9248e87283184d346aa9'
   r= requests.post('https://api.trello.com/1/cards',  params={'key': KEY, 'token': TOKEN, 'idList' : idList, 'name' : 'canoeing'})
   response = r.json()
   return response

@app.route('/getCard')
def getCard():
   cardId = '60afa040b07e9a4371098530'
   r= requests.get(f'https://api.trello.com/1/cards/{cardId}', params={'key': KEY, 'token': TOKEN})
   response=r.json()
   # cardName = response.name
   # print(cardName)
   return response     

@app.route('/addNewTitle',methods = ['POST'])
def addTitle():
   todo = request.form.get('nm')
   print(todo)
   idList = '60af9248e87283184d346aa9'
   r= requests.post('https://api.trello.com/1/cards',  params={'key': KEY, 'token': TOKEN, 'idList' : idList, 'name' : todo})
   response = r.json()
   # print("The response is:" + response)
   return redirect(url_for('index'))  
   


 
@app.route('/updateCard')
def updateCard():
   cardId = '60afa040b07e9a4371098530'
   # idList = '60af9248e87283184d346aaa'
   idList = '60af9fb7b29da277db69d121'
   r= requests.put(f'https://api.trello.com/1/cards/{cardId}',  params={'key': KEY, 'token': TOKEN, 'idList': idList})
   response = r.json()
   return response

app.run()
# updateCard()