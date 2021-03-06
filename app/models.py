from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote:
    '''
    Defining quotes object
    '''
    def __init__(self,author,quote,permalink):
        self.author = author
        self.quote = quote
        self.permalink = permalink



# class User(UserMixin,db.Model):
#     __tablename__ = 'users'
    
#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255),index = True)
#     email = db.Column(db.String(255),unique = True,index = True)
#     role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
#     password_hash = db.Column(db.String(255))

#     @property
#     def password(self):
#         raise AttributeError('You cannot read the password attribute')

#     @password.setter
#     def password(self, password):
#         self.pass_secure = generate_password_hash(password)

#     def verify_password(self,password):
#         return check_password_hash(self.pass_secure,password)


#     def __repr__(self):
#         return f'User {self.username}'



# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255))
#     users = db.relationship('User',backref = 'role',lazy="dynamic")


#     def __repr__(self):
#         return f'User {self.name}'


class Post:
    '''
    Defining quotes object
    '''
    def __init__(self,title,content):
        self.topic = title
        self.content = content

    
    all_posts = []

    def __init__(self,title,content):
        self.title = title
        self.content = content
    

    def save_post(self):
        Post.all_posts.append(self)


    @classmethod
    def clear_posts(cls):
        Post.all_posts.clear()

    @classmethod
    def get_posts(cls):

        response = []

        for post in cls.all_posts:
            response.append(post)

        return response

"""Database models."""
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = 'users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(100),
        nullable=False,
        unique=False
    )
    email = db.Column(
        db.String(40),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False
	)
    website = db.Column(
        db.String(60),
        index=False,
        unique=False,
        nullable=True
	)
    created_on = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )
    last_login = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)