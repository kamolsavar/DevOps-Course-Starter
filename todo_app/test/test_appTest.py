import pytest
import os
from flask import Flask
from dotenv import find_dotenv, load_dotenv
from todo_app.app import create_app
import requests
from unittest.mock import patch, Mock

TEST_BOARD_ID=os.getenv("BOARD_ID")

@pytest.fixture
def client():
 # Use our test integration config instead of the 'real' version
 file_path = find_dotenv('.env.test')
 load_dotenv(file_path, override=True)
 test_app = create_app()
 with test_app.test_client() as client:
  yield client

@patch('requests.get')
def test_index_page(mock_get_requests, client):
 # Replace call to requests.get(url) with our own function
 mock_get_requests.side_effect = mock_get_lists
 response = client.get('/')
 assert response.status_code ==200
 assert "Swimming" in response.data.decode()

sample_trello_card_response = [{"id":"card", "name":"Swimming", "idList":"1234todolist"}] 
# (card["id"], card["name"], status))

def mock_get_lists(url, params):
  if url == f'https://api.trello.com/1/boards/{TEST_BOARD_ID}/cards':
    response = Mock()
    print (response)
 # sample_trello_lists_response should point to some test response data
    response.json.return_value = sample_trello_card_response
    return response
  return None 