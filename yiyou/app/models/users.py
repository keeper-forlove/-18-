from app.extensions import db, login_manager
#导入UserMixin类
from flask_login import UserMixin
#导入密码散列及校验函数
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired

from app.models.comment import Comments


class Users(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    password_hash = db.Column(db.String(128),nullable=False)
    mail = db.Column(db.String(64),nullable=False)
    icon = db.Column(db.String(64),default='default.png')


    # 保护密码字段字段
    @property
    def password(self):
        raise AttributeError('密码不可读')

    #设置密码，加密后存储
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    #密码校验
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def get_comments(self):
        return Comments.objects.filter_by(uid=self.id)


# 登录认证回调
@login_manager.user_loader
def load_user(uid):
    return Users.query.get(int(uid))