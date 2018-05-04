from flask_restful import Resource
from models import StoreModel

class Store(Resource):
    def get(self, name):
        return StoreModel.find_by_name(name)

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "store already exists"}
        store = StoreModel(name)
        store.save_to_db()

    def delete(self, name):
        pass


class StoreList(Resource):
    def get(self, name):
        return {"stores": list(map(lambda x: x.json(), StoreModel.query.all()))}