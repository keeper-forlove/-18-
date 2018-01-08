from app.extensions import db
from datetime import datetime

class SpotComment(db.Model):
    __tablename__='spot_comments'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.utcnow)
    spotid = db.Column(db.Integer,db.ForeignKey('spots.id'))
    uid = db.Column(db.Integer,db.ForeignKey('users.id'))

class FoodsComment(db.Model):
    __tablename__='food_comments'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.utcnow)
    foodid = db.Column(db.Integer,db.ForeignKey('foods.id'))
    uid = db.Column(db.Integer,db.ForeignKey('users.id'))

class ShopsComment(db.Model):
    __tablename__='shop_comments'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.utcnow)
    shopid = db.Column(db.Integer,db.ForeignKey('shops.id'))
    uid = db.Column(db.Integer,db.ForeignKey('users.id'))

class HotelsComment(db.Model):
    __tablename__='hotel_comments'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.utcnow)
    hotelid = db.Column(db.Integer,db.ForeignKey('hotels.id'))
    uid = db.Column(db.Integer,db.ForeignKey('users.id'))