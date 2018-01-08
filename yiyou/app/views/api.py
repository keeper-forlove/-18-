from flask import request, jsonify
from flask.ext.restful import  Resource, abort

from app.extensions import db
from app.models import Country


class CoutryListApi(Resource):
    #获取国家列表
    def get(self):
        country_list = []
        country_all = Country.query.all()
        for country in country_all:
            data = {
                'id': country.id,
                'name': country.name
            }
            country_list.append(data)

        return jsonify({'country': country_list})

    #添加国家
    def post(self):
        # 查询该国家是否存在于数据库中
        countryname = request.json['name']
        country = Country.query.filter_by(name=countryname).all()
        # 如果存在
        if country:
            data = {
                'id': country[0].id,
                'name': country[0].name,
                'message': '%s已存在' % country[0].name
            }
        # 如果不存在
        else:
            # 添加到数据库
            country = Country(name=countryname)
            db.session.add(country)
            # 查询新添加的数据，获取其id
            country = Country.query.filter_by(name=countryname).all()[0]
            data = {
                'id': country.id,
                'name': country.name,
                'message': '%s添加成功' % countryname
            }
        return jsonify({'country': data})

    def delete(self, id):
        pass

class CoutryApi(Resource):
    def get(self, id):
        country = Country.query.filter_by(id=id).all()
        if len(country):
            data = {
                'id': country[0].id,
                'name': country[0].name}
            return jsonify({'country': data})

        else:
            abort(404)

    def put(self, id):
        pass

    def delete(self, id):
        country = Country.query.filter_by(id=id)
        db.session.delete(country)
        db.session.commit()
        return jsonify({'message':'成功删除%s'%country.name})



