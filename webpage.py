from flask import render_template, Flask, request, json
from database import *
app = Flask(__name__, static_folder='/Users/Main_Account/Documents/GitHub/Coding_Game')

@app.route('/')
def home():
    #print("loading home")
    return render_template('index.html')

@app.route('/_create_user', methods=["POST"])
def create():
    json = request.json
    username = json["username"]
    createUser(username)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)