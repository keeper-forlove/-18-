from flask import request, jsonify
from flask_restful  import  Resource

from app.extensions import db
from app.models import Users
from flask_login import current_user,login_user,logout_user,login_required


class RegisterApi(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        print(username,password,email)

        if Users.query.filter_by(username=username).count():

            data={
                'code':0,
                'message':'该用户名已被注册，请使用其他用户名！'
            }
        else:
            u = Users(username=username,password=password,mail=email)
            db.session.add(u)
            db.session.commit()
            data={
                'code':1,
                'message':'注册成功！',
                'username':username
            }
        return jsonify(data)

class LoginApi(Resource):

    def post(self):
        username = request.form['username']
        password = request.form['password']
        u = Users.query.filter_by(username=username).first()
        if not u:
            data={
                'code':0,
                'message':'用户不存在'
            }
        elif u.verify_password(password):
            data = {
                'code': 1,
                'message': '登录成功！'
            }
            login_user(u, remember=request.form.remember.data)

        else:
            data = {
                'code': 0,
                'message': '密码错误！'
            }

        return jsonify(data)