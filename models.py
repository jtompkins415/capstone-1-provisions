from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()


def connect_db(app):
    '''Connect to DB'''
    db.app = app
    db.init_app(app)

class User(db.Model):
    '''User Model'''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.VARCHAR(length=30), nullable = False, unique = True )
    email = db.Column(db.String, nullable = False, unique = True )
    first_name = db.Column(db.VARCHAR(length=50), nullable = False)
    last_name = db.Column(db.VARCHAR(length=50), nullable = False)
    password = db.Column(db.String, nullable = False)
    user_city = db.Column(db.String)
    user_state = db.Column(db.String)

    def __repr__(self):
        return f'<User id:{self.id} username:{self.username} first_name: {self.first_name} last_name: {self.last_name}>'
    
    @classmethod
    def register(cls,username,pwd,email,first_name,last_name, user_city, user_state):
        '''Register user and hash user's password'''

        hash = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hash.decode('utf8')

        return cls(username=username, password=hashed_utf8, email=email, first_name=first_name, last_name=last_name, user_city=user_city, user_state=user_state)

    
    @classmethod
    def authenticate(cls,username,pwd):
        '''Authenticate user'''

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, pwd):
            return user
        else:
            return False
    

class Beer(db.Model):
    '''Beer Model'''

    __tablename__ = 'beers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    beer_name = db.Column(db.String, nullable = False)
    brewery = db.Column(db.Integer, nullable=False)
    style = db.Column(db.String, nullable=False)
    abv = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String)

    def __repr__(self):
        return f'<Beer id:{self.id} beer_name:{self.beer_name} brewery:{self.brewery}>'

class Brewery(db.Model):
    '''Brewery Model '''        

    __tablename__ = 'breweries'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brewery_name = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    beers = db.Column(db.Integer, db.ForeignKey('beers.id'))

    def __repr__(self):
        return f'<Brewery id:{self.id} brewery_name:{self.brewery_name} city:{self.city} country:{self.country}>'

class Wine(db.Model):
    '''Wine Model'''

    __tablename__ = 'wines'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wine_name = db.Column(db.String, nullable=False)
    winery = db.Column(db.Integer, nullable=False)
    style = db.Column(db.String, nullable=False)
    vintage = db.Column(db.String, nullable=False)        
    abv = db.Column(db.Float, nullable=False)        
    price = db.Column(db.Float, nullable=False)        
    description = db.Column(db.String)

    def __repr__(self):
        return f'<Wine id:{self.id} wine_name:{self.wine_name} winery:{self.winery}>'


class Winery(db.Model):
    '''Winery Model'''

    __tablename__ = 'wineries'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    winery_name = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    wines = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Winery id:{self.id} winery_name:{self.winery_name} country:{self.country}>'

class Food(db.Model):
    '''Food Model'''

    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    producer = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String)
    wine_pairing = db.Column(db.Integer)
    beer_pairing = db.Column(db.Integer)

    def __repr__(self):
        return f'<Food id:{self.id} name:{self.name} producer:{self.producer} category:{self.category}>'        






