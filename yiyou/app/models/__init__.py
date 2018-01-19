#在其他路径，可以通过from .../models导入，而不需要.../models.xxx
# from . import articles,consumes,location,users,comment

from .articles import Experience,Questions
from .comment import Comments
from .location import City,Country
from .consumes import Foods,Shops,Spots,Hotels
from .users import Users
from app.extensions import db

#在__init__同级目录，可以通过from . import db导入
# from app.extensions import db

favorite = db.Table('favorite',
                    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                    db.Column('spots_id', db.Integer, db.ForeignKey('spots.id'))
                    )