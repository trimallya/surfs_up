# Dependencies
from flask import Flask

# Create new Flask app instance
app = Flask(__name__)

# Root route
@app.route('/')
def hello_world():
    return 'Hello World'

# New route
@app.route('/intro')
def name_intro():
    name = "Trisha"
    return f"Hi! My name is {name}. Welcome to my first flask page!"