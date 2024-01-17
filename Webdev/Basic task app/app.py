from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

#app is an instance of Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

#registering a route to the home page
@app.route('/')

def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug = True)
