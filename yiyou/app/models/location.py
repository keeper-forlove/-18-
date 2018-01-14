from app.extensions import db

class Country(db.Model):
    __tablename__='country'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=True,nullable=False)
    city = db.relationship('City', backref='country', lazy='dynamic')


class City(db.Model):
    __tablename__='city'
    id = db.Column(db.Integer,primary_key=True)
    label = db.Column(db.String(64),nullable=False)
    pinyin = db.Column(db.String(32),nullable=False)
    zip = db.Column(db.String(16),nullable=False)
    name = db.Column(db.String(64),nullable=False)
    countryid = db.Column(db.Integer,db.ForeignKey('country.id'))



