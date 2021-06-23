import os
from threading import Thread
import pytest
import requests
from selenium import webdriver
from todo_app.app import create_app

KEY=os.getenv("KEY")
TOKEN=os.getenv("TOKEN")

def create_trello_board():
    name = "To_Do_Test" 
    r=requests.post('https://api.trello.com/1/boards', params={'key': KEY, 'token': TOKEN, 'name' : {name}})

def delete_trello_board(self, board_id):
    self.board_id= board_id
    r=requests.delete('https://api.trello.com/1/boards/{board_id}', params={'key': KEY, 'token': TOKEN})

@pytest.fixture(scope='module')
def app_with_temp_board():
 # Create the new board & update the board id

# environment variable
 board_id = create_trello_board()
 os.environ['TRELLO_BOARD_ID'] = board_id
 # construct the new application
 application = create_app()
 # start the app in its own thread.
 thread = Thread(target=lambda:application.run(use_reloader=False))
 thread.daemon = True
 thread.start()
 yield application
 # Tear Down
 thread.join(1)
#  delete_trello_board(board_id)

@pytest.fixture(scope="module")
def driver():
 with webdriver.Firefox() as driver:
    yield driver

def test_task_journey(driver, app_with_temp_board):
 driver.get('http://localhost:5000/')
 assert driver.title == 'To-Do App' 
