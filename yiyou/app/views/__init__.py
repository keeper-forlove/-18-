
from .articals import article
# from .user import user

########################################    浩南    ################################
from .user import login,register,change_Password,change_mail,forget_Password,icon,info,favorite




# 蓝本配置
DEFAULT_BLUEPRINT = (
    # 蓝本，前缀
    (login, '/user'),
    (register,'/user'),
    (change_Password, '/user'),
    (change_mail, '/user'),
    (forget_Password, '/user'),
    (icon, '/user'),
    (info, '/user'),
    (favorite, '/user'),
    (article, '/article')
)


# 封装函数，完成蓝本注册
def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)


########################################   浩南   ################################
