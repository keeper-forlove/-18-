from flask import Blueprint, render_template, jsonify, request, abort

from app.extensions import db
from app.models import Users, Country


from flask import Flask, request, jsonify

main = Blueprint('main',__name__)

# @main.route('/')
# def welcome():
#     # u = Users.query.filter_by(id=1)
#     return 'hello,world!'
#
#
# #添加国家，例如：http://127.0.0.1:5000/addcountry/china
# @main.route('/addcountry/',methods=['POST'])
# def creat_country():
#     #查询该国家是否存在于数据库中
#     countryname=request.json['name']
#     country = Country.query.filter_by(name=countryname).all()
#     #如果存在
#     if country:
#         data={
#             'id':country[0].id,
#             'name':country[0].name,
#             'message':'%s已存在'%country[0].name
#         }
#     #如果不存在
#     else:
#         #添加到数据库
#         country = Country(name=countryname)
#         db.session.add(country)
#         #查询新添加的数据，获取其id
#         country = Country.query.filter_by(name=countryname).all()[0]
#         data = {
#             'id': country.id,
#             'name': country.name,
#             'message':'%s添加成功'%countryname
#         }
#     return jsonify({'country':data})
#
# #获取国家列表，例如：http://127.0.0.1:5000/countrylist/
# @main.route('/countrylist/')
# def country_list():
#     country_list = []
#     country_all = Country.query.all()
#     for country in country_all:
#         data = {
#             'id':country.id,
#             'name':country.name
#         }
#         country_list.append(data)
#
#     return jsonify({'country':country_list})
#
# #根据id获取指定国家，例如：http://127.0.0.1:5000/country/2
# @main.route('/getcountry/<int:id>')
# def get_country(id):
#     country = Country.query.filter_by(id=id).all()
#     if len(country):
#         data = {
#             'id': country[0].id,
#             'name': country[0].name}
#         return jsonify({'country': data})
#
#     else:
#         abort(404)
#
#
# # #定制错误页面df
# @main.errorhandler(404)
# def page_not_found(e):
#     return jsonify({'error':'page not found'}) ,404

