import os
from threading import Thread
import pytest
import certifi
import requests
from selenium import webdriver
from todo_app.app import create_app
from dotenv import find_dotenv, load_dotenv
import pymongo

@pytest.fixture(scope='module')
def app_with_temp_board():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    os.environ["DATABASE_NAME"]="selinum_database"
    application = create_app()
    thread = Thread(target=lambda:application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application
    client = pymongo.MongoClient(os.getenv("MONGO_DB_CONNECTION"), tlsCAFile=certifi.where())
    thread.join(1) 
    client.drop_database("selinum_database")
     

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
