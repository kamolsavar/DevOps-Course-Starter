import os
from threading import Thread
import pytest
import requests
from selenium import webdriver
from todo_app.app import create_app
from dotenv import find_dotenv, load_dotenv

@pytest.fixture(scope='module')
def app_with_temp_board():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    global KEY
    global TOKEN
    KEY=os.getenv("KEY")
    TOKEN=os.getenv("TOKEN")
    board_id = create_trello_board()
    os.environ["BOARD_ID"] = board_id
    os.environ["ID_LIST_TODO"] = ""
    os.environ["ID_LIST_DOING"] = ""
    os.environ["ID_LIST_DONE"] = ""

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
 opts = webdriver.ChromeOptions()
 opts.add_argument('--headless')
 opts.add_argument('--no-sandbox')
 opts.add_argument('--disable-dev-shm-usage')
 with webdriver.Chrome("./chromedriver", options=opts) as driver:
    yield driver

def test_task_journey(driver, app_with_temp_board):
 driver.get('http://localhost:5000/')
 assert driver.title == 'To-Do App' 
