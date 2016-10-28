from flask import Flask ,render_template
from sqlalchemy import *
from pyodbc import *

app = Flask(__name__)

@app.route("/")
def main() :
    return render_template("index.html")

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/main')
def home():
    return render_template('index.html')

@app.route('/showSearch')
def showSearch():
    return render_template('movieSearch.html')


if __name__ =="__main__":
    app.run()