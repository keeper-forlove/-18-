from flask import Blueprint,request,jsonify,session,current_app
from app.models import Users
from app.extensions import db
from flask_login import login_required,current_user

#对象的名称是让import来引入的,而括号里的则不是
shoppingCart = Blueprint('shoppingCart',__name__)

@shoppingCart.route('/order/<int:page>',methods = ['GET'])
@login_required
def userfavorite(page):
    u = current_user
    user_favorite = u.favorite
    spot_favorite_list = []
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
        spot_favorite_list.append(data)
    return jsonify({'spot_favorite_list':spot_favorite_list})
