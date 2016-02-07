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
    print(userid)
    if userExists(userid):
        session["userid"] = userid
    else:    
        createUser(userid)
    return "blank"

@app.route('/_logout', methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/_addXP', methods=["POST"])
def addXP():
    json = request.json
    amount = json["amount"]
    addExperience(session["userid"], amount)
    updateSession()

def updateSession():
    session["exp"] = getExperience(session["userid"]) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)