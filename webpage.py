from flask import render_template, Flask, request, json, session
from database import *
app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/_login', methods=["POST"])
def login():
    json = request.json
    userid = json["id"]
    if userExists(userid):
        session["userid"] = userids
    else:    
        createUser(username)
    return "blank"

@app.route('/_logout', methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/_addXP', methods=["POST"])
def addXP():
    json = request.json
    amount = json["amount"]
    addExperience(session["email"], amount)
    updateSession()

def updateSession():
    session["exp"] = getExperience(session["userid"]) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)