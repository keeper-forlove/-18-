from app.extensions import db

#导入UserMixin类
from flask_login import UserMixin
#导入密码散列及校验函数
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired


class Users(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    password_hash = db.Column(db.String(128),nullable=False)
    mail = db.Column(db.String(64),nullable=False)
    icon = db.Column(db.String(64),default='default.png')

    spot_comments = db.relationship('SpotComment',backref='user',lazy='dynamic')
    food_comments = db.relationship('FoodsComment',backref='user',lazy='dynamic')
    shop_comments = db.relationship('ShopsComment', backref='user',lazy='dynamic')
    hotel_comments = db.relationship('HotelsComment', backref='user',lazy='dynamic')

    experiences = db.relationship('Experience',backref='user',lazy='dynamic')


    #保护密码字段，proerty装饰器用于设置类的读方法
    @property
    def password(self):
        raise AttributeError('密码不可读')

    #设置密码，加密后存储，@password.setter装饰器，用于设置密码的写方法
    @password.setter
    def password(self,password):
        self.password_hash= generate_password_hash(password)

    #密码校验
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
