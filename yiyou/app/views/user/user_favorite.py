from flask import Blueprint,request,jsonify,session,current_app
from app.models import Users
from app.extensions import db
from flask_login import login_required,current_user

#对象的名称是让import来引入的,而括号里的则不是
favorite = Blueprint('favorite',__name__)

@favorite.route('/favorite/<int:page>',methods = ['GET'])
@login_required
def userfavorite(page):
    u = current_user
    user_favorite = u.favorite
    favorite_list = []
    start = (page - 1) * 10
    end = page * 10
    data = {}
    spot_list = u.favorite[start:end]
    for spot in spot_list:
        data = {
            'name':spot.name,
            'city':spot.city,
            'adress':spot.adress,
            'detail':spot.detail,
            'price':spot.price
        }

        favorite_list.append(data)
    return jsonify({'spot_favorite_list':favorite_list})

@favorite.route('/changefavorite/<int:sid>',methods = ['GET'])
@login_required
def add_del_favorite(sid):
    if current_user.is_favorite(sid):
        current_user.del_favorite(sid)
        data = {'code': 0, 'msg': '取消收藏成功'}
        return jsonify(data)
    else:
        current_user.add_favorite(sid)
        data = {'code': 1, 'msg': '收藏成功'}
        return jsonify(data)

