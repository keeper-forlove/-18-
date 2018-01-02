from app.extensions import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    password_hash = db.Column(db.String(128),nullable=False)
    mail = db.Column(db.String(64),nullable=False)
    icon = db.Column(db.String(64),default='default.png')

    spot_comments = db.relationship('spot_comments',backref='user',lazy='dynamic')
    food_comments = db.relationship('food_comments',backref='user',lazy='dynamic')
    shop_comments = db.relationship('shop_comments', backref='user',lazy='dynamic')
    hotel_comments = db.relationship('hotel_comments', backref='user',lazy='dynamic')

    experiences = db.relationship('experience',backref='user',lazy='dynamic')
