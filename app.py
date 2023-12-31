"""Module hello word"""
from flask import Flask

app = Flask(__name__)

"""Print hello word"""
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=8001, host="0.0.0.0")
