import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models import ItemModel


class Item(Resource):
    TABLE_NAME = "items"

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type=float,
        required=True,
        help="this field cannot be left blank"
    )
    parser.add_argument(
        "store_id",
        type=float,
        required=True,
        help="An item needs to belong to a store"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        else:
            return {"item": None}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name) is not None:
            return {"message": "Item already exists"}, 403
        else:
            data = Item.parser.parse_args()
            item = ItemModel(name, **data)
            item.save_to_db()
            return item.json(), 200


class ItemList(Resource):
    def get(self):
        return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}