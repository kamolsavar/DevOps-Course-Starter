import pytest
from flask import Flask
from dotenv import find_dotenv, load_dotenv
from todo_app.app import create_app
@pytest.fixture
def client():
 # Use our test integration config instead of the 'real' version
 file_path = find_dotenv('.env.test')
 load_dotenv(file_path, override=True)
 test_app = create_app()
 # Use the app to create a test_client that can be used in our   
 with test_app.test_client() as client:
  yield client

def test_index_page(client):
 response = client.get('/')
 