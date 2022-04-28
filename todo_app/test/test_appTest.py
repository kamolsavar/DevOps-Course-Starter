import pytest
import os
import certifi
from flask import Flask
from dotenv import find_dotenv, load_dotenv
from todo_app.app import create_app
import requests
import mongomock
import pymongo
from unittest.mock import patch, Mock

@pytest.fixture
def client():
 # Use our test integration config instead of the 'real' version
 file_path = find_dotenv('.env.test')
 load_dotenv(file_path, override=True)
 with mongomock.patch(servers=(('fakemongo.com', 27017),)): 
  test_app = create_app()
  with test_app.test_client() as client:
    yield client


def test_index(client):       
  mock_mongo_db_connection = pymongo.MongoClient(os.getenv("MONGO_DB_CONNECTION"),tlsCAFile=certifi.where())
  db = mock_mongo_db_connection[os.getenv('DATABASE_NAME')] 
  collection = db.test_collection
  mock_record = collection.insert_one({"Name": "Boxing", "Status": "To Do" })
  response=client.get('/')
  assert response.status_code==200
  assert 'Boxing' in response.data.decode()

  