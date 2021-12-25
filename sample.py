from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World"

# how to rename a file in VS Code, it's complicated