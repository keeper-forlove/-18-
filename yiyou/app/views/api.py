from flask import request, jsonify
from flask_restful  import  Resource, abort
from flask_login import current_user,login_user,logout_user,login_required
from app.extensions import db
from app.models import Country, City, Spots, Foods, Hotels, Shops

####################################################获取国家列表、添加国家####################################################

class CoutryListApi(Resource):
    #get方式获取国家列表
    #请求地址：http://127.0.0.1:5000/country/
    #返回数据格式：{"countrylist": [{"id": 10,"name": "china"},{"id": 11,"name": "japan"}]}
    def get(self):
        print(request.args['name'])
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
    @login_required
    #需要登录才能调用
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

####################################################获取指定国家、删除国家####################################################
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
    # @login_required
    #需要登录才能调用
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

####################################################获取城市列表、添加新城市####################################################

class CityListApi(Resource):

    #get方法获取所有city
    #请求地址：http://127.0.0.1:5000/city/
    #响应结果：{ "citylist": [{"country": 10,"id": 4,"name": "hangzhou"},{"country": 10,"id": 5,"name": "beijing"}]}
    def get(self):
        city_list=[]
        city_all = City.query.all()
        for city in city_all:
            country = Country.query.filter_by(id=city.countryid).first()
            data={
                'id':city.id,
                'name':city.name,
                'country':country.name
            }
            city_list.append(data)
        return jsonify({'citylist':city_list})

    #post方法添加城市
    #请求地址：http://127.0.0.1:5000/city/
    #数据请求格式：{"name":"shenzhen","countryid":10}
    #返回数据格式：
    #{"code": 0,"message": "beijing已存在！"}
    #{"code": 1,"country": 13,"id": 10,"message": "shanghai添加成功","name": "shanghai"}
    # @login_required
    #需要登录才能调用
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
            country=Country.query.filter_by(id=city.countryid).first()
            data = {
                'code':1,
                'id':city.id,
                'name':city.name,
                'country':country.name,
                'message': '%s添加成功' % city.name
            }
        return jsonify(data)

####################################################获取城市、删除城市####################################################
class CityApi(Resource):
    #通过id获取指定城市
    #请求地址：http://127.0.0.1:5000/city/<int:id>
    #响应数据：{"city": { "code": 1,"country": null,"id": 5,"message": "成功查询到beijing","name": "beijing"}}
    #{"city": {"code": 0,"message": "没有该城市！"}}
    def get(self,id):
        city = City.query.filter_by(id=id).first()
        if city:
            country = Country.query.filter_by(id=city.countryid).first()
            data = {
                'id':city.id,
                'name':city.name,
                'country':country.name,
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
    # @login_required
    #需要登录才能调用
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

####################################################通过类别查询所有城市数据####################################################

#根据category参数(spots、hotels、food、shops)获取数据，page为分页参数
class ConsumesListApi(Resource):

    type_dir={
        'spots':Spots(),
        'food':Foods(),
        'shops':Shops(),
        'hotels':Hotels()
    }

    def get(self,category):
        page=int(request.args['page'])
        start = (page-1)*10
        end = page*10
        #根据category和page获取相应的数据对象的列表
        obj_list = self.type_dir[category].query.all()[start:end]
        data = {}
        if not len(obj_list):
            data={
                'code':0,
                'message':'没有数据'
            }
        #遍历列表中的数据对象，将其字段取出存入字典
        else:
            data_list = []
            for obj in obj_list:
                item_data={
                    'id':obj.id,
                    'name':obj.name,
                    'city':City.query.filter_by(id=obj.city).first().name,
                    'provience': obj.type,
                    'adress':obj.adress,
                    'price':obj.price,
                    'img_url_list':obj.pictures.split(','),
                    'detail': obj.detail
                }
                data_list.append(item_data)
            data={
                'code':1,
                'message':'查询成功',
                'list':data_list
            }

        return jsonify(data)

####################################################通过类别获取数据，并通过city参数和page参数进行筛选####################################################

class ConsumesListByCityApi(Resource):
    type_dir={
        'spots':Spots(),
        'food':Foods(),
        'shops':Shops(),
        'hotels':Hotels()
    }

    #根据city获取景点数据，page为分页参数
    def get(self,category):
        city=request.args['city']
        page=int(request.args['page'])
        modelObj = self.type_dir[category]
        start = (page - 1) * 10
        end = page * 10

        city = City.query.filter_by(pinyin=city).first()
        #判断，如果城市名不存在
        if not city:
            data={
                'code':0,
                'message':'该城市名没有被记录！请查询其他城市！'
            }
        #如果城市存在
        else:
            cityid = city.id
            obj_list = modelObj.query.filter_by(city=cityid)[start:end]
            #如果查询到指定页面数据
            if len(obj_list):
                data_list = []
                for obj in obj_list:
                    obj_data = {
                        'id': obj.id,
                        'name': obj.name,
                        'city': City.query.filter_by(id=obj.city).first().name,
                        'provience': obj.type,
                        'adress': obj.adress,
                        'price': obj.price,
                        'img_url_list': obj.pictures.split(','),
                        'detail': obj.detail
                    }
                    data_list.append(obj_data)

                data={
                    'code':1,
                    'message':'成功查询到数据！',
                    'spot_list':data_list
                }
            #如果没有指定页面数据
            else:
                data={
                    'code':0,
                    'message':'没有查询到数据！'
                }

        return jsonify(data)
