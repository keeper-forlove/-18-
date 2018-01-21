from flask import Flask, jsonify
from app.config import config
from app.extensions import config_extensions
from app.views import config_blueprint

#导入restful模块和相关资源类
from flask.ext.restful import Api
from app.views.api import CoutryListApi, CoutryApi, CityListApi, CityApi, SpotsListApi, SpotsByCityApi, HotelsByCityApi, \
    HotelsListApi, FoodslsListApi, FoodsByCityApi, ExperiencelsListApi, ExperienceByCityApi, ShopslsListApi, \
    ShopByCityApi


def create_app(config_name):
    #创建应用实例
    app= Flask(__name__)
    #初始化配置
    app.config.from_object(config.get(config_name) or config[ 'default'])
   #调用初始化函数
    config[config_name].init_app(app)
    #调用扩展初始化函数
    config_extensions(app)
    #配置蓝本
    config_blueprint(app)
    # 自定义错误页面
    config_errorhandler(app)

    #初始化api
    api = Api(app)
    api.add_resource(CoutryListApi, '/country','/country/')
    api.add_resource(CoutryApi, '/country/<int:id>')
    api.add_resource(CityListApi, '/city/')
    api.add_resource(CityApi, '/city/<int:id>')
    api.add_resource(SpotsListApi,'/spots/','/spotss')
    api.add_resource(SpotsByCityApi,'/spots/<string:city>','/spots/<string:city>/')
    api.add_resource(HotelsListApi,'/hotels/','/hotels')
    api.add_resource(HotelsByCityApi,'/hotels/<string:city>','/hotels/<string:city>/')
    api.add_resource(FoodslsListApi,'/foods/','/foods')
    api.add_resource(FoodsByCityApi,'/foods/<string:city>','/foods/<string:city>/')
    api.add_resource(ExperiencelsListApi,'/experiences/','/experiences')
    api.add_resource(ExperienceByCityApi,'/experiences/<string:city>','/experiences/<string:city>/')
    api.add_resource(ShopslsListApi,'/shops/','/shops')
    api.add_resource(ShopByCityApi,'/shops/<string:city>','/shops/<string:city>/')

    # api.init_app(app)

    # 返回应用实例
    return app


def config_errorhandler(app):
    # 如果在蓝本中定制只针对本蓝本中的错误有效
    #可以使用app_errorhandler定制全局错误页面
    @app.errorhandler(404)
    def page_not_found(e):
        data = {'code':1,'message': 'page not found'}
        return jsonify(data)

    @app.errorhandler(403)
    def page_not_found(e):
        data = {'code':2,'message': 'Forbidden'}
        return jsonify(data)

    @app.errorhandler(400)
    def page_not_found(e):
        data = {'code':2,'message': '请求错误'}
        return jsonify(data)

    @app.errorhandler(401)
    def page_not_found(e):
        data = {'code':3,'message': '需要登陆才能访问'}
        return jsonify(data)


    @app.errorhandler(405)
    def page_not_found(e):
        data = {'code':4,'message': '请求方式错误'}
        return jsonify(data)

