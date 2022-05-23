from datetime import datetime

from extensions import db, login_manager
from app import app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Books(db.Model):
    __tablename__ = "Books"
    id = db.Column(db.Integer(), primary_key= True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50), unique = True)
    price = db.Column(db.Integer())
    description = db.Column(db.Text)
    image_url = db.Column(db.Text)
    is_in_stock = db.Column(db.Boolean)
    genre = db.Column(db.String(30))
    language = db.Column(db.String(30))
    publisher = db.Column(db.String(50))

    def __repr__(self):
        return self.title

    def __init__(self, title, author, description, language, publisher, price,  is_in_stock, image_url, genre):
        self.title = title
        self.author = author
        self.price = price
        self.description = description
        self.image_url = image_url
        self.is_in_stock = is_in_stock
        self.genre = genre
        self.language = language
        self.publisher = publisher

    def save(self):
        db.session.add(self)
        db.session.commit()


class User_comment(db.Model):
    __tablename__ = "User_comment"
    id = db.Column(db.Integer(), primary_key= True)
    username = db.Column(db.String(30), unique = True,  nullable = False)
    user_comment = db.Column(db.Text,  nullable = False)
    comment_date = db.Column(db.DateTime, default=datetime.utcnow)
    book_id = db.Column(db.Integer, db.ForeignKey('Books.id'), nullable=False)


    def __repr__(self):
        return self.title

    def __init__(self, username, user_comment, book_id ):
        self.username = username
        self.user_comment = user_comment
        self.book_id = book_id


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    surname = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(30), nullable = False, unique = True)
    username = db.Column(db.String(30), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
    is_active = db.Column(db.Boolean, nullable = False)
    is_superuser = db.Column(db.Boolean, nullable = False)

    def __init__(self, name, surname, email, username, password, is_active = True, is_superuser = False) :
        self.name = name
        self.surname = surname
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.is_active = is_active
        self.is_superuser = is_superuser

    def save(self):
        db.session.add(self)
        db.session.commit()


    def check_password(self, password):
        return check_password_hash(self.password, password)





# Book6 = Books(title = "Sapiens", author = "harari", price = 13, description = "Some text", image_url = "https://m.media-amazon.com/images/I/51Sn8PEXwcL.jpg", is_in_stock = True, genre= "Novel", language = "Az" ,publisher= "Qanun")