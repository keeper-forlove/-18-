from app.extensions import db
import os
from flask import Blueprint,request,url_for,jsonify,current_app,render_template
import random
from flask_login import login_required,current_user
from PIL import Image

icon = Blueprint('icon',__name__)



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']


def random_string(length = 32):
    base_string = '1230456789zqwertyuiopasdfghjklxcvbnm'
    return  ''.join(random.choice(base_string) for i in range(length))


@icon.route('/icon/', methods=['POST'])
# @login_required
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        suffix = os.path.splitext(file.filename)[1]
        filename = random_string() + suffix
        file.save(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], filename))
        pathname = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], filename)
        img = Image.open(pathname)
        img.thumbnail((128, 128))
        img.save(pathname)
        # current_user.icon = pathname
        # db.session.add(current_user)
        data = {'code': 0, 'message': '头像上传成功'}
        return jsonify(data)
    else:
        data = {'code': 1, 'message': '头像格式错误'}
        return jsonify(data)

@icon.route('/qqq/', methods=['GET'])
# @login_required
def aaa():
    return render_template('test.html')





