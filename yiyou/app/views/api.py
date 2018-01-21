from flask import request, jsonify
from flask_restful  import  Resource, abort
from flask_login import current_user,login_user,logout_user,login_required
from app.extensions import db
from app.models import Country, City, Spots, Hotels, Foods, Experience, Shops


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

################################################  获取景点数据  ################################################

class SpotsListApi(Resource):
    #获取所有景点数据，page为分页参数
    def get(self):
        order=None
        try:
            order = request.args.get('order')
        except:
            pass
        page =int(request.args.get('page',1))
        limit=int(request.args.get('limit',10))
        start = (page-1)*limit
        end = page*limit

        if page < 1 or limit < 0:
            data = {
                'code': 0,
                'type':'spots',
                'message': '参数不合法'
            }
            return jsonify(data)

        if (page-1)*limit>=Spots.query.count():
            data={
                'code':0,
                'type': 'spots',
                'message':'没有数据'
            }
        else:
            if order:
                spot_list = Spots.query.order_by(db.asc(order))[start:end]
            else:
                spot_list = Spots.query.all()[start:end]
            data_list =[]
            for spot in spot_list:
                spot_data={
                    'id':spot.id,
                    'name':spot.name,
                    'city':City.query.filter_by(id=spot.city).first().name,
                    'provience': spot.type,
                    'adress':spot.adress,
                    'price':spot.price,
                    'img_url_list':spot.pictures.split(','),
                    'detail': spot.detail,
                    'score':spot.score,
                    'rank':spot.rank,
                    'commens':spot.comments
                }
                data_list.append(spot_data)

            data={
                'code':'1',
                'type': 'spots',
                'message':'成功！',
                'data_list':data_list
            }

        return jsonify(data)



# -----------------------------------------------  通过城市获取景点数据  -----------------------------------------------#

class SpotsByCityApi(Resource):
    #根据city获取景点数据，page为分页参数
    def get(self,city):
        order=None
        try:
            order = request.args.get('order')
        except:
            pass
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        start = (page - 1) * limit
        end = page * limit

        city = City.query.filter_by(pinyin=city).first()
        #判断，如果城市名不存在
        if not city:
            data={
                'code':0,
                'type': 'spots',
                'message':'没有该城市！'
            }
        #如果城市存在
        else:
            cityid = city.id
            if order:
                s_list = Spots.query.filter_by(city=cityid).order_by(db.asc(order))[start:end]
            else:
                s_list = Spots.query.filter_by(city=cityid)[start:end]
            # s_list = Spots.query.filter_by(city=cityid)[start:end]

            #如果查询到指定页面数据
            if len(s_list):
                spot_list = []
                for spot in s_list:
                    spot_data = {
                        'id': spot.id,
                        'name': spot.name,
                        'city': City.query.filter_by(id=spot.city).first().name,
                        'provience': spot.type,
                        'adress': spot.adress,
                        'price': spot.price,
                        'img_url_list': spot.pictures.split(','),
                        'detail': spot.detail,
                        'score': spot.score,
                        'rank': spot.rank,
                        'commens': spot.comments
                    }
                    spot_list.append(spot_data)

                data={
                    'code':1,
                    'type': 'spots',
                    'message':'成功查询到数据！',
                    'spot_list':spot_list
                }
            #如果没有指定页面数据
            else:
                data={
                    'code':0,
                    'type': 'spots',
                    'message':'没有数据！'
                }

        return jsonify(data)

################################################  获取酒店数据  ################################################

class HotelsListApi(Resource):
    #获取所有景点数据，page为分页参数
    def get(self):
        order = None
        try:
            order = request.args.get('order')
        except:
            pass
        page =int(request.args.get('page',1))
        limit=int(request.args.get('limit',10))
        start = (page-1)*limit
        end = page*limit
        if page<1 or limit<0:
            data={
                'code':0,
                'type': 'hotel',
                'message':'参数不合法'
            }
            return jsonify(data)

        if (page-1)*limit>=Hotels.query.count():
            data={
                'code':0,
                'type': 'hotel',
                'message':'没有数据了！'
            }
        else:
            if order:
                hotel_list = Hotels.query.order_by(db.asc(order))[start:end]
            else:
                hotel_list = Hotels.query.all()[start:end]
            # hotel_list = Hotels.query.all()[start:end]
            data_list =[]
            for hotel in hotel_list:
                spot_data={
                    'id':hotel.id,
                    'name':hotel.name,
                    'city':City.query.filter_by(id=hotel.city).first().name,
                    'provience': hotel.type,
                    'adress':hotel.adress,
                    'price':hotel.price,
                    'img_url_list':hotel.pictures.split(','),
                    'detail': hotel.detail,
                    'score': hotel.score,
                    'rank': hotel.rank,
                    'commens': hotel.comments
                }
                data_list.append(spot_data)

            data={
                'code':'1',
                'type': 'hotel',
                'message':'成功！',
                'data_list':data_list
            }

        return jsonify(data)

#-----------------------------------------------  通过城市获取酒店数据  -----------------------------------------------#

class HotelsByCityApi(Resource):
    # 根据city获取景点数据，page为分页参数
    def get(self, city):
        order = None
        try:
            order = request.args.get('order')
        except:
            pass
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        start = (page - 1) * limit
        end = page * limit

        if page < 1 or limit < 0:
            data = {'code': 0,'type':'hotel','message': '参数不合法'}
            return jsonify(data)

        city = City.query.filter_by(pinyin=city).first()
        # 判断，如果城市名不存在
        if not city:
            data = {'code': 0,'type':'hotel','message': '该城市名没有被记录！请查询其他城市！'}
        # 如果城市存在
        else:
            cityid = city.id
            if order:
                h_list = Hotels.query.filter_by(city=cityid).order_by(db.asc(order))[start:end]
            else:
                h_list =Hotels.query.filter_by(city=cityid)[start:end]
            # h_list = Hotels.query.filter_by(city=cityid)[start:end]
            # 如果查询到指定页面数据
            if len(h_list):
                hotel_list = []
                for hotel in h_list:
                    hotel_data = {
                        'id': hotel.id,'name': hotel.name,
                        'city': City.query.filter_by(id=hotel.city).first().name,
                        'provience': hotel.type,
                        'adress': hotel.adress,
                        'price': hotel.price,
                        'img_url_list': hotel.pictures.split(','),
                        'detail': hotel.detail,
                        'score': hotel.score,
                        'rank': hotel.rank,
                        'commens': hotel.comments
                    }
                    hotel_list.append(hotel_data)

                data = {'code': 1,'type':'hotel','message': '成功！','hotel_list': hotel_list}
            # 如果没有指定页面数据
            else:
                data = {'code': 0,'type':'hotel','message': '没有数据'}

        return jsonify(data)


################################################  获取商店/购物数据  ################################################

class ShopslsListApi(Resource):
    # 获取所有景点数据，page为分页参数
    def get(self):
        order = None
        try:
            order = request.args.get('order')
        except:
            pass
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        start = (page - 1) * limit
        end = page * limit
        if page < 1 or limit < 0:
            data = {
                'code': 0,
                'type': 'shop',
                'message': '参数不合法'
            }
            return jsonify(data)

        if (page - 1) * limit >= Shops.query.count():
            data = {
                'code': 0,
                'type': 'shop',
                'message': '没有数据！'
            }
        else:
            if order:
                shop_list = Shops.query.order_by(db.asc(order))[start:end]
            else:
                shop_list = Shops.query.all()[start:end]
            # food_list = Foods.query.all()[start:end]
            data_list = []
            for shop in shop_list:
                shop_data = {
                    'id': shop.id,
                    'name': shop.name,
                    'city': City.query.filter_by(id=shop.city).first().name,
                    'provience': shop.type,
                    'adress': shop.adress,
                    'price': shop.price,
                    'img_url_list': shop.pictures.split(','),
                    'detail': shop.detail,
                    'score': shop.score,
                    'commens': shop.comments
                }
                data_list.append(shop_data)

            data = {
                'code': '1',
                'type': 'shop',
                'message': '成功！',
                'data_list': data_list
            }

        return jsonify(data)

# -----------------------------------------------  通过城市获取购物数据  -----------------------------------------------#

class ShopByCityApi(Resource):
    # 根据city获取景点数据，page为分页参数
    def get(self, city):
        order = None
        try:
            order = request.args.get('order')
        except:
            pass
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        start = (page - 1) * limit
        end = page * limit

        if page < 1 or limit < 0:
            data = {'code': 0, 'message': '参数不合法'}
            return jsonify(data)

        city = City.query.filter_by(pinyin=city).first()
        # 判断，如果城市名不存在
        if not city:
            data = {'code': 0,'type': 'food', 'message': '该城市名没有被记录！请查询其他城市！'}
        # 如果城市存在
        else:
            cityid = city.id
            if order:
                f_list = Shops.query.filter_by(city=cityid).order_by(db.asc(order))[start:end]
            else:
                f_list =Shops.query.filter_by(city=cityid)[start:end]
            # f_list = Foods.query.filter_by(city=cityid)[start:end]
            # 如果查询到指定页面数据
            if len(f_list):
                shop_list = []
                for shop in f_list:
                    shop_data = {
                        'id': shop.id, 'name': shop.name,
                        'city': City.query.filter_by(id=shop.city).first().name,
                        'provience': shop.type,
                        'adress': shop.adress,
                        'price': shop.price,
                        'img_url_list': shop.pictures.split(','),
                        'detail': shop.detail,
                        'score': shop.score,
                        'commens': shop.comments
                    }
                    shop_list.append(shop_data)

                data = {'code': 1, 'type': 'shop','message': '成功！', 'food_list': shop_list}
            # 如果没有指定页面数据
            else:
                data = {'code': 0, 'type': 'shop','message': '没有数据'}

        return jsonify(data)


################################################  获取美食数据  ################################################

class FoodslsListApi(Resource):
    # 获取所有景点数据，page为分页参数
    def get(self):
        order = None
        try:
            order = request.args.get('order')
        except:
            pass
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        start = (page - 1) * limit
        end = page * limit
        if page < 1 or limit < 0:
            data = {
                'code': 0,
                'type': 'food',
                'message': '参数不合法'
            }
            return jsonify(data)

        if (page - 1) * limit >= Foods.query.count():
            data = {
                'code': 0,
                'type': 'food',
                'message': '没有数据了！'
            }
        else:
            if order:
                food_list = Foods.query.order_by(db.asc(order))[start:end]
            else:
                food_list = Foods.query.all()[start:end]
            # food_list = Foods.query.all()[start:end]
            data_list = []
            for food in food_list:
                food_data = {
                    'id': food.id,
                    'name': food.name,
                    'city': City.query.filter_by(id=food.city).first().name,
                    'provience': food.type,
                    'adress': food.adress,
                    'price': food.price,
                    'img_url_list': food.pictures.split(','),
                    'detail': food.detail,
                    'score': food.score,
                    'commens': food.comments
                }
                data_list.append(food_data)

            data = {
                'code': '1',
                'type': 'food',
                'message': '成功！',
                'data_list': data_list
            }

        return jsonify(data)

# -----------------------------------------------  通过城市获取美食数据  -----------------------------------------------#

class FoodsByCityApi(Resource):
    # 根据city获取景点数据，page为分页参数
    def get(self, city):
        order = None
        try:
            order = request.args.get('order')
        except:
            pass
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        start = (page - 1) * limit
        end = page * limit

        if page < 1 or limit < 0:
            data = {'code': 0, 'message': '参数不合法'}
            return jsonify(data)

        city = City.query.filter_by(pinyin=city).first()
        # 判断，如果城市名不存在
        if not city:
            data = {'code': 0,'type': 'food', 'message': '该城市名没有被记录！请查询其他城市！'}
        # 如果城市存在
        else:
            cityid = city.id
            if order:
                f_list = Foods.query.filter_by(city=cityid).order_by(db.asc(order))[start:end]
            else:
                f_list =Foods.query.filter_by(city=cityid)[start:end]
            # f_list = Foods.query.filter_by(city=cityid)[start:end]
            # 如果查询到指定页面数据
            if len(f_list):
                food_list = []
                for food in f_list:
                    food_data = {
                        'id': food.id, 'name': food.name,
                        'city': City.query.filter_by(id=food.city).first().name,
                        'provience': food.type,
                        'adress': food.adress,
                        'price': food.price,
                        'img_url_list': food.pictures.split(','),
                        'detail': food.detail,
                        'score': food.score,
                        'commens': food.comments
                    }
                    food_list.append(food_data)

                data = {'code': 1, 'type': 'food','message': '成功！', 'food_list': food_list}
            # 如果没有指定页面数据
            else:
                data = {'code': 0, 'type': 'food','message': '没有数据'}

        return jsonify(data)

################################################  获取所有游记  ################################################

class ExperiencelsListApi(Resource):
    # 获取所有游记，page为分页参数
    def get(self):
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        start = (page - 1) * limit
        end = page * limit
        if page < 1 or limit < 0:
            data = {
                'code': 0,
                'type': 'experience',
                'message': '参数不合法'
            }
            return jsonify(data)

        if (page - 1) * limit >= Experience.query.count():
            data = {
                'code': 0,
                'type': 'experience',
                'message': '没有数据了！'
            }
        else:
            experience_list = Experience.query.all()[start:end]
            data_list = []
            for experience in experience_list:
                experience_data = {
                    'id': experience.id,
                    'uid': experience.uid,
                    'city': experience.city,
                    'title': experience.title,
                    'content': experience.content,
                    'create_time': experience.create_time,
                    'type': experience.type,
                }
                data_list.append(experience_data)

            data = {
                'code': '1',
                'type': 'experience',
                'message': '成功！',
                'data_list': data_list
            }

        return jsonify(data)



# -----------------------------------------------  通过城市获取游记  -----------------------------------------------#

class ExperienceByCityApi(Resource):
    # 根据city获取景点数据，page为分页参数
    def get(self, city):
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        start = (page - 1) * limit
        end = page * limit

        if page < 1 or limit < 0:
            data = {'code': 0, 'message': '参数不合法'}
            return jsonify(data)

        city = City.query.filter_by(pinyin=city).first()
        # 判断，如果城市名不存在
        if not city:
            data = {'code': 0,'type': 'experience', 'message': '该城市名没有被记录！请查询其他城市！'}
        # 如果城市存在
        else:
            experience_list = Experience.query.all()[start:end]
            data_list = []
            # 如果查询到指定页面数据
            if len(experience_list):
                for experience in experience_list:
                    experience_data = {
                        'id': experience.id,
                        'uid': experience.uid,
                        'city': experience.city,
                        'title': experience.title,
                        'content': experience.content,
                        'create_time': experience.create_time,
                        'type': experience.type,
                    }
                    data_list.append(experience_data)

                data = {'code': 1, 'type': 'experience','message': '成功！', 'data_list': data_list}
            # 如果没有指定页面数据
            else:
                data = {'code': 0, 'type': 'experience','message': '没有数据'}

        return jsonify(data)