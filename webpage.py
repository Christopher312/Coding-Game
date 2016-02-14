from flask import render_template, Flask, request, json, session
from database import *
import sys

app = Flask(__name__, static_folder='static')

#testcases = "[\"2 3\", \"4 9\"]"
testcases= [2, 6, 16]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    print("hi")
    print("home", session["userid"])
    print(getExperience(session["userid"]))
    return render_template('home.html', exp=getExperience(session["userid"]))

@app.route('/problems', methods=['GET'])
def problems():
    return render_template('problems.html')

@app.route('/_problem', methods=["POST"])
def problem():
    l = request.json["results"]
    #source = json["source"]
    #lang = json["lang"]
    #tryCase(source, lang, testcases)
    print(l)
    correct = True;
    for i in range(len(l)):
        if l[i] != testcases[i]:
            correct = False
    if correct:
        addExperience(session["userid"], amount)
    print(correct)
    return str(correct)

@app.route('/codemonprofile', methods=['GET'])
def profile():
    return render_template('codemonprofile.html')

@app.route('/_login', methods=["POST"])
def login():
    json = request.json
    userid = json["id"]        
    print("hi 1")
    print("login", userid)
    if userExists(userid):
        print("exists")
        try:
            session["userid"] = userid
        except:
            e = sys.exc_info()[0]
            print(e)
        print("hi 1")
    else:
        print("doesn't exists")    
        insertUser(userid)
        session["userid"] = userid
        print("hi 2")
    print("userid from session", session["userid"])
    return "ok"

@app.route('/_logout', methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for('home'))
'''
@app.route('/_addXP', methods=["POST"])
def addXP():
    json = request.json
    amount = json["amount"]
    addExperience(session["userid"], amount)
    updateSession()
'''

if __name__ == '__main__':
    app.secret_key = 'NOTVERYSECRET'
    app.run(host='0.0.0.0', debug=True)