from flask import Flask, redirect, url_for,  render_template
from todo_app.data import session_items
from todo_app.flask_config import Config
from flask import request
import requests

app = Flask(__name__)
app.config.from_object(Config)

KEY= '350982ff516536af2c1918c3281d6abf'
TOKEN ='6ace7390733d2990a38ac5d8f66465cec75f24b525c522a6c5d6a02a218b3d9a'
payload = {'key': KEY, 'token': TOKEN}


@app.route('/index')
def index():
    list = session_items.get_items()
    return  render_template('index.html', list=list)

@app.route('/createBoard')
def createBoard():
   name='ToDoList'
   r= requests.post('https://api.trello.com/1/boards', params={'key': KEY, 'token': TOKEN, 'name': name})
   response=r.json()
   return response  

@app.route('/getBoard')
def getBoard():
   id = '60af9248e87283184d346aa8'
   r= requests.get(f'https://api.trello.com/1/boards/{id}', params=payload)
   response=r.json()
   return response     

@app.route('/createCardList')
def createCardList():
   name='Monday'
   boardId= '60af9248e87283184d346aa8'
   r= requests.post(f'https://api.trello.com/1/boards/{boardId}/lists',  params={'key': KEY, 'token': TOKEN, 'name': name})
   response=r.json()
   return response  


@app.route('/createCard')
def createCard(self):
   idList = '60af9fb7b29da277db69d121'
   r= requests.post('https://api.trello.com/1/cards',  params={'key': KEY, 'token': TOKEN, 'idList' : idList})
   response = r.json()
   return response

@app.route('/getCard')
def getCard():
   cardId = '60afa040b07e9a4371098530'
   r= requests.get(f'https://api.trello.com/1/cards/{cardId}', params=payload)
   response=r.json()
   return response     
 
@app.route('/updateCard')
def updateCard():
   cardId = '60afa040b07e9a4371098530'
   r= requests.put(f'https://api.trello.com/1/cards/{cardId}',  params={'key': KEY, 'token': TOKEN, 'name' : 'Running'})
   response = r.json()
   return response

app.run()