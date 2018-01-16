from flask import Blueprint, render_template
from app.extensions import db


from flask import Flask, request, jsonify

main = Blueprint('main',__name__)

# @main.route('/')
# def welcome():
#     # u = Users.query.filter_by(id=1)
#     return 'hello,world!'

#
#
# # #定制错误页面df
# @main.errorhandler(404)
# def page_not_found(e):
#     return jsonify({'error':'page not found'}) ,404

