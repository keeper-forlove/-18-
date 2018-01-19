from flask import Blueprint,request,jsonify,session,current_app
from app.models import Users
from app.extensions import db
from flask_login import current_user,login_required
from app.email import send_mail

info = Blueprint('info',__name__)

@info.route('/userinfo/',methods = ['GET'])
@login_required
def userinfo():
    if current_user.confirmed:
        state = '已激活'
    else:
        state = '未激活'
    data = {
        '用户名称':current_user.username,
        '绑定邮箱':current_user.mail,
        '激活状态':state,
        'icon':current_user.icon
    }
    return jsonify(data)

