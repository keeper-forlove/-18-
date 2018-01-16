from app.extensions import db
from datetime import datetime

class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.utcnow)
    type=db.Column(db.String(20),nullable=False)
    tid = db.Column(db.Integer,nullable=False)
    uid = db.Column(db.Integer,nullable=False)
