from app import app
#from flask import Flask # from the flask module import Flask module

#app = Flask(__name__)   # create an instance of the Flask class

@app.route("/")   # define decorator that maps view functions to routes
def index():    # view functiion
    me = {  # dictionary# python dictionary
        "first_name": "Fernanda",   
        "last_name": "Ugalde",
        "hobbies": "dance",
        "is_online": True
    }
    return me   # when you return a dict from a view function, it becomes JSON