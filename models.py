from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()



db = SQLAlchemy()


class User(db.Model):
    '''User Model'''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(30), nullable = False, unique = True )
    email = db.Column(db.String, nullable = False, unique = True )
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String, nullable = False)
    user_city = db.Column(db.String)
    user_state = db.Column(db.String)

    
    
    
    def __repr__(self):
        return f'User id:{self.id} username:{self.username} first_name: {self.first_name} last_name: {self.last_name}'




def connect_db(app):
    '''Connect to DB'''
    db.app = app
    db.init_app(app)

