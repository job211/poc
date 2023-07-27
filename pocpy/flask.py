'''
Ce POC utilise Flask, un micro-framework Python, pour créer 
une API HTTP basique qui renvoie "Hello, World!" lorsque vous 
accédez à l'URL racine.
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a simple API POC.'

if __name__ == '__main__':
    app.run()
