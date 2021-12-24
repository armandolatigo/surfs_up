# Skill Drill 9.4.3
from flask import Flask
app = Flask(__name__)
@app.route('/')
def person():
    person = input("Who?: ")
    return (f'Oh you mean {person}')