from app.extensions import db
from app.models import Comments


class Spots(db.Model):
    __tablename__='spots'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    city = db.Column(db.Integer,db.ForeignKey('city.id'))
    detail = db.Column(db.Text,nullable=True)
    adress = db.Column(db.String(100),nullable=False)
    score = db.Column(db.Integer,nullable=False,default=5)
    pictures = db.Column(db.Text,nullable=False)
    price =db.Column(db.Integer,nullable=False)
    type = db.Column(db.String(20),nullable=True)
    rank = db.Column(db.Integer,nullable=True,default=5)

    @property
    def comments(self):
        commens_obj= Comments.query.filter_by(type='spots',tid =self.id)
        return [(commen.uid,commen.create_time,commen.content) for commen in commens_obj]


class Foods(db.Model):
    __tablename__='foods'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    city = db.Column(db.Integer, db.ForeignKey('city.id'))
    describe = db.Column(db.Text,nullable=True)
    adress = db.Column(db.String(100),nullable=False)
    score = db.Column(db.Integer,nullable=False,default=5)
    pictures = db.Column(db.Text,default='food_default.png')
    price =db.Column(db.Integer,nullable=False)
    type = db.Column(db.String(20),nullable=True)

    @property
    def comments(self):
        commens_obj = Comments.query.filter_by(type='foods', tid=self.id)
        return [(commen.uid, commen.create_time, commen.content) for commen in commens_obj]


class Shops(db.Model):
    __tablename__='shops'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    city = db.Column(db.Integer, db.ForeignKey('city.id'))
    describe = db.Column(db.Text,nullable=True)
    adress = db.Column(db.String(100),nullable=False)
    score = db.Column(db.Integer,nullable=False,default=5)
    pictures = db.Column(db.Text,default='shop_default.png')
    price =db.Column(db.Integer,nullable=False)
    type = db.Column(db.String(20),nullable=True)

    @property
    def comments(self):
        commens_obj = Comments.query.filter_by(type='shops', tid=self.id)
        return [(commen.uid, commen.create_time, commen.content) for commen in commens_obj]


class Hotels(db.Model):
    __tablename__='hotels'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    city = db.Column(db.Integer, db.ForeignKey('city.id'))
    describe = db.Column(db.Text,nullable=True)
    adress = db.Column(db.String(100),nullable=False)
    score = db.Column(db.Integer,nullable=False,default=5)
    pictures = db.Column(db.Integer,default='hotel_default.png')
    price =db.Column(db.Integer,nullable=False)
    type = db.Column(db.String(20),nullable=True)
    rank = db.Column(db.Integer,nullable=True,default=5)

    @property
    def comments(self):
        commens_obj = Comments.query.filter_by(type='hotels', tid=self.id)
        return [(commen.uid, commen.create_time, commen.content) for commen in commens_obj]

