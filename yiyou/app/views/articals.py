from flask import Blueprint, render_template
from flask import Flask, request, jsonify

from app.extensions import db
from app.models import Comments
from app.models.articles import Experience

article = Blueprint('article',__name__)


@article.route('/comments',methods=['POST'])
def write_comment():
    if request.method=='POST':
        content=request.form['content']
        type=request.form['type'] #文章类型（景点/酒店/美食）
        tid=request.form['tid']   #(景点/酒店/美食）对应的id
        uid=request.form['uid']
        comment =Comments(content=content,type=type,tid=tid,uid=uid)
        db.session.add(comment)
        return jsonify({'code':1,'message':'创建成功'})

@article.route('/experience',methods=['POST'])
def write_experience():
    if request.method=='POST':
        uid = request.form['uid']
        type = request.form['type']
        city = request.form['city']
        title = request.form['title']
        content = request.form['content']
        experience =Experience(uid=uid,type=type,city=city,title=title,content=content)
        db.session.add(experience)
        return jsonify({'code':1,'message':'创建成功'})
