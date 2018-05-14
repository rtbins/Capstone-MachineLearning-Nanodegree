from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from resources import Item, UserRegister, ItemList, Store, StoreList

from security import authenticate, identity

app = Flask(__name__)

app.secret_key = "to the milky way"

app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

JWT(app, authenticate, identity)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Item, "/item/<string:name>")
api.add_resource(UserRegister, "/userregister" )
api.add_resource(ItemList, "/items" )
api.add_resource(Store, "/store/<string:name>" )
api.add_resource(StoreList, "/stores" )

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)start_date = datetime.datetime(2012, 1, 1)
end_date = datetime.datetime(2017, 1, 1)
ford = pd.read_csv('Ford_Stock.csv', index_col='Date', parse_dates=True)

ford = ford.loc[(ford.index >= start_date) & (ford.index <= end_date)]start_date = datetime.datetime(2012, 1, 1)
end_date = datetime.datetime(2017, 1, 1)
ford = pd.read_csv('Ford_Stock.csv', index_col='Date', parse_dates=True)

ford = ford.loc[(ford.index >= start_date) & (ford.index <= end_date)]