from db import db

class UserModel(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def get_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(username=name).first()
