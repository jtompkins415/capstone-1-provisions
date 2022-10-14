from flask import Flask, render_template, redirect, flash, session, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config['SECRET_KEY'] = "prOvisions123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)

@app.route('/', methods=['GET'])
def redirect_home():
    '''Redirect root route to homepage'''

    return redirect('/provisions/home')

@app.route('/provisions/home', methods=['GET'])
def show_home_page():
    '''Render landing page'''

    return render_template('home.html')