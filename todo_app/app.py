from flask import Flask,  render_template
from todo_app.data import session_items
from todo_app.flask_config import Config

list = ['Harry Potter', 'Sherlock Holmes', 'Dino Master']

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html', list = list)

@app.route('/addTitles')
def addTitle():
    return session_items.add_item('Never Land')
def getTitle():
    return session_items.get_item('4')         

if __name__ == '__main__':
    app.run()
