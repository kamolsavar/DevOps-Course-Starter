from flask import Flask,  render_template
from todo_app.data import session_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addList')
def addList():
    return render_template('indexList.html')

@app.route('/addTitles')
def addTitle():
    return session_items.add_item(title)

if __name__ == '__main__':
    app.run()
