from flask import Blueprint,request,jsonify,session,current_app
from app.models import Users
from app.extensions import db
from app.email import send_mail



register = Blueprint('register',__name__)

@register.route('/register/',methods = ['POST'])
def registering():
    username = request.get_json(True).get("username")
    password = request.get_json(True).get("password")
    mail = request.get_json(True).get("mail")
    # username = request.data["username"]
    # password = request.data["password"]
    # mail = request.data["mail"]
    if username and password and mail:
        if Users.query.filter_by(username=username).first():
            data = {'code': 1, 'message': '该用户已经存在,请更换用户名'}
            return jsonify(data)
        elif Users.query.filter_by(mail=mail).first():
            return jsonify({'code': 2, 'message': '此邮箱已注册,请更换邮箱'})
        u = Users(username=username,password=password,mail=mail)
        db.session.add(u)
        #因为要用到id，所以这里必须进行手动提交
        db.session.commit()
        token = u.generate_activate_token()
        send_mail(mail, '账户激活','email/password',username=username,token=token)
        data = {'code': 3, 'message': '请前往邮箱激活账号'}
        return jsonify(data)
    else:
        data = {'code': 0, 'message': '请填写空缺数据'}
        return jsonify(data)

@register.route('/activate/<token>',methods = ['GET','POST'])
def activate(token):
    return Users.check_activate_token(token)

