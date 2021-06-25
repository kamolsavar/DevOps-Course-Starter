import os
from threading import Thread
import pytest
import requests
from selenium import webdriver
from todo_app.app import create_app

KEY=os.getenv("KEY")
TOKEN=os.getenv("TOKEN")

@pytest.fixture(scope='module')
def app_with_temp_board():
    board_id = create_trello_board()
    os.environ["BOARD_ID"] = board_id
    os.environ["ID_LIST_TODO"] = "60d5eb000d11e46a91a68424"
    os.environ["ID_LIST_DOING"] = "60d5eb000d11e46a91a68425"
    os.environ["ID_LIST_DONE"] = "60d5eb000d11e46a91a68424"

    application = create_app()
    thread = Thread(target=lambda:application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application
    delete_trello_board(board_id)
    thread.join(1)  

def create_trello_board():
    name = "To_Do_Test" 
    response=requests.post('https://api.trello.com/1/boards', params={'key': KEY, 'token': TOKEN, 'name' : name})
    return response.json()["id"]

def delete_trello_board(board_id):
    r=requests.delete(f'https://api.trello.com/1/boards/{board_id}', params={'key': KEY, 'token': TOKEN})

@pytest.fixture(scope="module")
def driver():
 with webdriver.Firefox() as driver:
    yield driver

def test_task_journey(driver, app_with_temp_board):
 driver.get('http://localhost:5000/')
 assert driver.title == 'To-Do_Test' 
