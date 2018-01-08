#在其他路径，可以通过from .../models导入，而不需要.../models.xxx
# from . import articles,consumes,location,users,comment
from .users import Users
from .articles import Experience,Questions
from .comment import ShopsComment,SpotComment,FoodsComment,HotelsComment
from .location import City,Country
from .consumes import Foods,Shops,Spots,Hotels

#在__init__同级目录，可以通过from . import db导入
# from app.extensions import db