from flask import Flask, render_template, redirect, flash, session, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Beer, Brewery, Wine, Winery


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///provisions_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "provisions415"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/', methods=['GET'])
def redirect_home():
    '''Redirect root route to homepage'''

    return redirect('/provisions/home')

@app.route('/provisions/home', methods=['GET'])
def show_home_page():
    '''Render landing page'''

    return render_template('home.html')