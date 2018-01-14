#导入类库
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_login import LoginManager


#创建对象
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
moment = Moment()
migrate = Migrate(db=db)
login_manager = LoginManager()

#初始化
def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    migrate.init_app(app)


    # 登录认证
    login_manager.init_app(app)
    # 指定登录的端点
    login_manager.login_view = '/login/'
    # 需要登录才能访问的提示信息
    login_manager.login_message = '需要登录才能访问'
    # 设置session保护级别
    # None:禁用sesssion保护
    # 'basic':基本保护，默认选项
    # 'strong':最严格的保护，一旦用户登录信息发生改变,立即退出登录
    login_manager.session_protection = 'strong'
