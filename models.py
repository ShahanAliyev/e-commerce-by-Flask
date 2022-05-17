from datetime import datetime
from email.policy import default

from flask import session

from extensions import db
from app import app


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


# Book6 = Books(title = "Sapiens", author = "harari", price = 13, description = "Some text", image_url = "https://m.media-amazon.com/images/I/51Sn8PEXwcL.jpg", is_in_stock = True, genre= "Novel", language = "Az" ,publisher= "Qanun")