from flask import Blueprint,request,jsonify,session,current_app
from app.models import Users
from app.extensions import db
from flask_login import current_user,login_required
from app.email import send_mail


forget_Password = Blueprint('forget_Password',__name__)

@forget_Password.route('/forgetpassword/',methods = ['POST'])
def forgetPassword():
    username_or_mail = request.get_json(True).get("username_or_mail")
    password_new = request.get_json(True).get("password_new")
    if username_or_mail and password_new:
        u_username = Users.query.filter_by(username=username_or_mail).first()
        u_mail = Users.query.filter_by(mail=username_or_mail).first()
        if u_username:
            if u_username.confirmed:
                token = u_username.generate_forgetpassword_token(password_new)
                send_mail(u_username.mail, '找回密码', 'email/forgetpassword', username=username_or_mail, token=token)
                data = {'code': 0, 'message': '请前往绑定邮箱修改密码','id':u_username.id}
                return jsonify(data)
            else:
                data = {'code': 2, 'message': '修改失败,用户邮箱未激活'}
                return jsonify(data)
        elif u_mail:
            if u_mail.confirmed:
                token = u_mail.generate_forgetpassword_token(password_new)
                send_mail(u_mail.mail, '找回密码', 'email/forgetpassword', username=username_or_mail, token=token)
                data = {'code': 0, 'message': '请前往绑定邮箱修改密码', 'id': u_username.id}
                return jsonify(data)
            else:
                data = {'code': 2, 'message': '修改失败,用户邮箱未激活'}
                return jsonify(data)
        else:
            data = {'code': 3, 'message': '用户名或邮箱不存在'}
            return jsonify(data)
    else:
        data = {'code':1,'message':'数据格式错误'}
        return jsonify(data)

@forget_Password.route('/gopassword/<token>',methods = ['GET','POST'])
def change(token):
    return Users.forget_possword_token(token)