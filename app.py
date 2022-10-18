from flask import Flask, current_app, render_template, redirect, flash, session, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Beer, Brewery, Wine, Winery
from forms import UserForm


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///provisions-db'
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

##USER ROUTE

@app.route('/provisions/user/new', methods=['GET', 'POST'])
def show_user_form():
    '''Render User creation form and handle submition'''

    form = UserForm()

    if form.validate_on_submit():
        new_user = User(
            username = form.username.data,
            password = form.password.data,
            email = form.email.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            user_city = form.user_city.data,
            user_state = form.user_state.data
            )
        
        db.session.add(new_user)
        db.session.commit()

        return redirect('/provisions/home')
    
    return render_template('sign-up.html', form=form)