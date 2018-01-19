from flask import Blueprint,request,jsonify,session,current_app
from app.models import Users
from app.extensions import db
from flask_login import current_user,login_required
from app.email import send_mail

change_mail = Blueprint('change_mail',__name__)

@change_mail.route('/changeMail/',methods = ['POST'])
@login_required
def changemail():
    mail_old = request.get_json(True).get("mail_old")
    mail_new = request.get_json(True).get("mail_new")
    u = current_user
    # u = Users.query.filter_by(mail=current_user.mail).first()
    if mail_old == u.mail:
        token = u.generate_changemail_token(mail_new)
        send_mail(mail_new, '修改绑定邮箱','email/email',username=u.username,token=token)
        data = {'code': 0, 'message': '请前往新邮箱确认修改'}
        return jsonify(data)
    else:
        data = {'code': 1, 'message': '原邮箱账号错误'}
        return jsonify(data)


@change_mail.route('/change/<token>',methods = ['GET','POST'])
def change(token):
    return Users.change_mail_token(token)