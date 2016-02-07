from flask import render_template, Flask, request, json
from database import *
app = Flask(__name__, static_folder='/Users/Main_Account/Documents/GitHub/Coding_Game')

@app.route('/')
def home():
    #print("loading home")
    return render_template('index.html')

@app.route('/_login', methods=["POST"])
def login():
    json = request.json
    username = json["username"]
    createUser(username)

@app.route('/_increase_exp', methods=["POST"])
def increaseExp():
    json = request.json
    increase = json[""]


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)