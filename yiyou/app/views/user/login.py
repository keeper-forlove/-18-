from flask import Blueprint,request,jsonify,session,current_app
from app.models import Users
from app.extensions import db
from flask_login import login_user,logout_user,login_required

login = Blueprint('login',__name__)

@login.route('/login/',methods = ['POST'])
def loging():
    username_or_mail = request.get_json(True).get("username_or_mail")
    password = request.get_json(True).get("password")
    # username_or_mail = request.data["username_or_mail"]
    # password = request.data["password"]
    # mail = request.get_json(True).get('mail')
    if username_or_mail and password:
        u_username = Users.query.filter_by(username=username_or_mail).first()
        u_mail = Users.query.filter_by(mail=username_or_mail).first()
        if u_username:
            if u_username.confirmed:
                if username_or_mail == u_username.username and u_username.verify_password(password):
                    login_user(u_username)
                    data = {'code': 1, 'message': '登陆成功','id':u_username.id}
                    return jsonify(data)
                else:
                    data = {'code': 0, 'message': '用户名与密码不匹配'}
            else:
                data = {'code': 0, 'message': '登录失败,用户邮箱未激活'}
                return jsonify(data)

        elif u_mail:
            if u_mail.confirmed:
                if username_or_mail == u_mail.mail and u_mail.verify_password(password):
                    login_user(u_mail)
                    data = {'code': 1, 'message': '登陆成功'}
                    return jsonify(data)
                else:
                    data = {'code': 0, 'message': '邮箱与密码不匹配'}
                    return jsonify(data)
            else:
                data = {'code': 0, 'message': '登录失败,用户邮箱未激活'}
                return jsonify(data)
        else:
            data = {'code': 0, 'message': '用户名或邮箱不存在'}
            return jsonify(data)
    else:
        data = {'code':0,'message':'数据格式错误'}
        return jsonify(data)

@login.route('/logout/',methods = ['GET','POST'])
def logout():
    logout_user()
    data = {'code': 0, 'message': '退出登陆'}
    return jsonify(data)

@login.route('/test/',methods = ['GET','POST'])
@login_required
def test():
    return '666'