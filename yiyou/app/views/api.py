from flask import request, jsonify
from flask_restful  import  Resource, abort

from app.extensions import db
from app.models import Country, City

class CoutryListApi(Resource):
    #get方式获取国家列表
    #请求地址：http://127.0.0.1:5000/country/
    #返回数据格式：{"countrylist": [{"id": 10,"name": "china"},{"id": 11,"name": "japan"}]}
    def get(self):
        country_list = []
        country_all = Country.query.all()
        for country in country_all:
            data = {
                'id': country.id,
                'name': country.name
            }
            country_list.append(data)

        return jsonify({'countrylist': country_list})

    #post方法添加国家
    #请求地址：http://127.0.0.1:5000/country/
    #请求数据格式：{"name":"china","countryid":10}
    #返回数据格式：
    #{"code": 1, "id": 15,"message": "japan添加成功","name": "japan"}
    #{"code": 0,"message": "该国家已存在！"}
    def post(self):
        # 查询该国家是否存在于数据库中
        countryname = request.json['name']
        country = Country.query.filter_by(name=countryname).first()
        # 如果存在
        if country:
            data={
                'code':0,
                'message':'该国家已存在！'
            }
        # 如果不存在,则先插入数据
        else:
            # 添加到数据库
            country = Country(name=countryname)
            db.session.add(country)
            #再次查询并取出数据
            country = Country.query.filter_by(name=countryname).first()
            data = {
                'code':1,
                'id': country.id,
                'name': country.name,
                'message': '%s添加成功' % country.name
            }
        return jsonify(data)


class CoutryApi(Resource):
    #GET方法根据id获取指定国家
    #请求地址：http://127.0.0.1:5000/country/<int:id>
    #返回数据：
    #{"code": 1,"id": 13,"message": "成功获取china","name": "china"}
    #{"code": 0,"message": "该国家不存在"}
    def get(self, id):
        country = Country.query.filter_by(id=id).first()
        if country:
            data = {
                'code':1,
                'id': country.id,
                'name': country.name,
                'message':'成功获取%s'%country.name
            }
        else:
            data={
                'code':0,
                'message':'该国家不存在'
            }
        return jsonify(data)

    #delete方法根据id删除指定国家
    #请求地址：http://127.0.0.1:5000/country/<int:id>
    #返回数据：
    #{"code": 1,"message": "成功删除japan"}
    #{"code": 0,"message": "该国家不存在"}
    def delete(self, id):
        country = Country.query.filter_by(id=id).first()
        if country:
            db.session.delete(country)
            db.session.commit()
            data={
                'code':1,
                'message':'成功删除%s'%country.name
            }
        else:
            data={
                'code':0,
                'message':'该国家不存在！'
            }
        return jsonify(data)



class CityListApi(Resource):

    #get方法获取所有city
    #请求地址：http://127.0.0.1:5000/city/
    #响应结果：{ "citylist": [{"country": 10,"id": 4,"name": "hangzhou"},{"country": 10,"id": 5,"name": "beijing"}]}
    def get(self):
        city_list=[]
        city_all = City.query.all()
        for city in city_all:
            data={
                'id':city.id,
                'name':city.name,
                'country':city.countryid
            }
            city_list.append(data)
        return jsonify({'citylist':city_list})

    #post方法添加城市
    #请求地址：http://127.0.0.1:5000/city/
    #数据请求格式：{"name":"shenzhen","countryid":10}
    #返回数据格式：
    #{"code": 0,"message": "beijing已存在！"}
    #{"code": 1,"country": 13,"id": 10,"message": "shanghai添加成功","name": "shanghai"}
    def post(self):
        name = request.json['name']
        countryname = request.json['countryname']
        country = Country.query.filter_by(name=countryname).first()
        city = City.query.filter_by(name=name).first()
        if city:
            data={
                'code':0,
                'message':'%s已存在！'%name
            }
        else:
            city = City(name=name,countryid=country.id)
            db.session.add(city)
            city=City.query.filter_by(name=name).first()
            data = {
                'code':1,
                'id':city.id,
                'name':city.name,
                'country':city.countryid,
                'message': '%s添加成功' % city.name
            }
        return jsonify(data)

class CityApi(Resource):
    #通过id获取指定城市
    #请求地址：http://127.0.0.1:5000/city/<int:id>
    #响应数据：{"city": { "code": 1,"country": null,"id": 5,"message": "成功查询到beijing","name": "beijing"}}
    #{"city": {"code": 0,"message": "没有该城市！"}}
    def get(self,id):
        city = City.query.filter_by(id=id).first()
        if city:
            data = {
                'id':city.id,
                'name':city.name,
                'country':city.countryid,
                'message':'成功查询到%s'%city.name,
                'code':1
            }
        else:
            data={
                'message':'没有该城市！',
                'code':0
            }
        return jsonify({'city':data})

    #通过id删除指定城市
    #请求地址：http://127.0.0.1:5000/city/<int:id>
    #响应数据：{"code": 0,"message": "成功删除beijing"}
    #{"code": 0,"message": "城市不存在"}
    def delete(self,id):
        city = City.query.filter_by(id=id).first()
        if city:
            db.session.delete(city)
            db.session.commit()
            data={
                'message': '成功删除%s' % city.name,
                'code':1
            }
        else:
            data = {
                'message': '城市不存在',
                'code': 0
            }
        return jsonify(data)




