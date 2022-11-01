from flask import Flask, current_app, render_template, redirect, flash, session, request, jsonify, g
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Beer, Brewery, Wine, Winery
from forms import UserForm, LoginForm


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///provisions-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "provisions415"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

#LANDING PAGE ROUTES

@app.route('/', methods=['GET'])
def redirect_home():
    '''Redirect root route to homepage'''

    return redirect('/provisions/home')

@app.route('/provisions/home', methods=['GET'])
def show_home_page():
    '''Render landing page'''
    
    return render_template('home.html')

@app.route('/provisions/about-us', methods=['GET'])
def show_about_us():
    '''Render About Us page'''

    return render_template('about-us.html')


@app.route('/provisions/contact-us', methods=['GET'])
def show_contact_us():
    '''Render Contact page'''

    return render_template('contact-us.html')
#SEED COMMAND

@app.cli.command('seed')
def seed():
    db.drop_all()
    db.create_all()
    rachel = User(username="rachelgurl235", email="rachel.adams916@gmail.com", first_name="Rachel", last_name="Adams", password="password1", user_city="Sacramento", user_state="CA")
    doug = User(username="superdrinker34", email="douggydogg@gmail.com", first_name="Doug", last_name="Jones", password="password2", user_city="Los Angeles", user_state= "CA")
    felix = User(username="felixthecat233", email="felixthecat@yahoo.com", first_name="Felix", last_name="Bower", password="password3", user_city="New Orleans", user_state="LA")
    gina = User(username="winelover98", email="gina.rochelle40@aol.com", first_name="Gina", last_name="Harrison", password="password4", user_city="Salt Lake City", user_state="UT")
    morgan = User(username="runandchug32", email="morgan.dunnigan@hotmail.com", first_name="Morgan", last_name="Dunnigan", password="password5", user_city="Burmingham", user_state="AL")
    lewis = User(username="lewisbiggulp60", email="lewis.killigan@gmail.com", first_name="Lewis", last_name="Killigan", password="password6", user_city="Seattle", user_state="WA")

    db.session.add_all([rachel, doug, felix, gina, morgan, lewis])
    db.session.commit()
    print('SEED COMPLETE!')


##USER ROUTE

@app.route('/provisions/user/new', methods=['GET', 'POST'])
def show_user_form():
    '''Render User creation form and handle submition'''

    form = UserForm()
    
    if form.validate_on_submit():
        new_user = User.register(
            username = form.username.data,
            pwd = form.password.data,
            email = form.email.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            user_city = form.user_city.data,
            user_state = form.user_state.data
            )
        
        db.session.add(new_user)
        db.session.commit()

        flash('User Created!')

        return redirect(f'/provisions/user/${new_user.username}')
        
    
    return render_template('sign-up.html', form=form)


@app.route('/provisions/user/signin', methods=['GET', 'POST'])
def user_signin():
    '''Render user sign in form and handle submission'''

    form = LoginForm()
    # import pdb
    # pdb.set_trace()
    if form.validate_on_submit():
        username = form.username.data
        pwd = form.password.data

        user = User.authenticate(username, pwd)
        if user:
            flash(f'Welcome back, {user.username}')
            session['username'] = user.username
            return redirect(f'/provisions/user/{user.id}')
        else:
            form.username.errors = ['Invalid username/password']

    return render_template('login.html', form=form)


@app.route('/provisions/user/logout', methods=['GET'])
def logout_user():
    '''Logout user and remove themn from the session'''

    session.pop('username')
    return redirect('/')

@app.route('/provisions/user/<id>', methods=['GET'])
def user_details(id):
    '''Show details about logged in User'''
    user = User.query.get_or_404(id)

    if user.username != session['username']:
        flash('Login Required')
        return redirect('/provisions/user/signin')
    else:
        return render_template('user-details.html', user=user) 


### SHOP ROUTES

@app.route('/provisions/shop', methods=['GET'])
def shop_home():
    '''Render shop landing page'''

    return render_template('shop-home.html')

@app.route('/provisions/shop/cart', methods=['GET'])
def show_shopping_cart():
    '''Render Shopping Cart'''

    return render_template('cart.html')