from flask import Blueprint,request,jsonify,session,current_app
from app.models import Users
from app.extensions import db
from flask_login import current_user,login_required


change_Password = Blueprint('change_Password',__name__)

@change_Password.route('/changePassword/',methods = ['POST'])
@login_required
def checkpassword():
    request
    password_old = request.get_json(True).get("password_old")
    password_new = request.get_json(True).get("password_new")
    u = current_user
    # u = Users.query.filter_by(username=current_user.username).first()
    if u.verify_password(password_old):
        u.password = password_new
        db.session.add(u)
        data = {'code': 0, 'message': '密码修改成功'}
        return jsonify(data)
    else:
        data = {'code': 1, 'message': '原密码错误'}
        return jsonify(data)
