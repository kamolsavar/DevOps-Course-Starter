import pytest
from flask import Flask


def create_app():
 app = Flask(__name__)
 # We specify the full path and remove the import for this config so 
 # it loads the env variables when the app is created, rather than 
# when this file is imported 
 app.config.from_object('todo_app.flask_config.Config')
 # All the routes and setup code etc
 return app

@pytest.fixture
def client():
 # Use our test integration config instead of the 'real' version
 file_path = find_dotenv('.env.test')
 load_dotenv(file_path, override=True)
 # Create the new app.
 test_app = app.create_app()
 # Use the app to create a test_client that can be used in our 
# tests.with 
 
test_app.test_client() as client:
  yield client

def test_index_page(client):
 response = client.get('/')
 