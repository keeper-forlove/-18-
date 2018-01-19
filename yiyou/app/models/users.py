from app.extensions import login_manager, db
from flask import current_app, jsonify
# 导入UserMixin类
from flask_login import UserMixin
# 导入密码散列及校验函数
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired
from itsdangerous import SignatureExpired, BadSignature
from app.models.consumes import Spots


# from app.models import Users


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    mail = db.Column(db.String(64), nullable=False, unique=True)
    icon = db.Column(db.String(64), default='default.png')
    confirmed = db.Column(db.Boolean, default=False)
    wallet = db.Column(db.Integer, nullable=False, default=0)

    # 多对多
    favorite = db.relationship('Spots', secondary='favorite', backref=db.backref('users', lazy='dynamic'),
                                    lazy='dynamic')

    # shopping_car = db.relationship('Shoppingcar', secondary='shopping', backref=db.backref('users', lazy='dynamic'),
    #                                lazy='dynamic')

    # 保护密码字段，proerty装饰器用于设置类的读方法
    @property
    def password(self):
        raise AttributeError('密码不可读')

    # 设置密码，加密后存储，@password.setter装饰器，用于设置密码的写方法
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 密码校验
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 获取token，激活账户
    def generate_activate_token(self, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in)
        return s.dumps({'id': self.id})

    # 修改邮箱，获取token
    def generate_changemail_token(self, email, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in)
        return s.dumps({'id': self.id, 'username': self.username, 'email': email})

    # 忘记密码，获取token，前往邮箱改密
    def generate_forgetpassword_token(self, new_password, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in)
        return s.dumps({'id': self.id, 'username': self.username, 'new_password': new_password})

    @staticmethod
    def check_activate_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except BadSignature:
            data = '失效的密钥'
            return data
        except SignatureExpired:
            data = '密钥已失效'
            return data
        user = Users.query.get(data.get('id'))
        if not user:
            data = '激活账户不存在'
            return data
        if not user.confirmed:
            user.confirmed = True
            db.session.add(user)
            data = '账户激活成功,请前往登陆页面登陆'
            return data

    @staticmethod
    def change_mail_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except BadSignature:
            data = '失效的密钥'
            return data
        except SignatureExpired:
            data = '密钥已失效'
            return data
        user = Users.query.get(data.get('id'))
        if not user:
            data = '修改邮箱账户不存在'
            return data
        new_mail = data.get('email')
        user.mail = new_mail
        db.session.add(user)
        data = '账户邮箱修改成功'
        return data

    @staticmethod
    def forget_possword_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except BadSignature:
            data = '失效的密钥'
            return data
        except SignatureExpired:
            data = '密钥已失效'
            return data
        user = Users.query.get(data.get('id'))
        if not user:
            data = '修改密码账户不存在'
            return data
        new_password = data.get('new_password')
        user.password = new_password
        db.session.add(user)
        data = '账户密码修改成功'
        return data

    def is_favorite(self, sid):
        sid = int(sid)
        favorites = self.favorite.all()
        for spot in favorites:
            if spot.id == sid:
                return True
                # spots = list(filter(lambda s: s.id == sid,favorites))
                # if len(spots) > 0:
            else:
                return False

    def add_favorite(self, sid):
        p = Spots.query.get(sid)
        self.favorite.append(p)

    def del_favorite(self, sid):
        p = Spots.query.get(sid)
        self.favorite.remove(p)


# 登陆认证回掉
@login_manager.user_loader
def load_user(uid):
    return Users.query.get(int(uid))