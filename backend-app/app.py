from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db
from flask_cors import CORS

from resources import UserRegister, StockData, Predict

from security import authenticate, identity

app = Flask(__name__)

app.secret_key = "to the milky way"

app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

JWT(app, authenticate, identity)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(StockData, "/stockData/<string:name>")
api.add_resource(UserRegister, "/userregister" )

# prediction models
# date details should be in header
api.add_resource(Predict, "/predict/<string:model>")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True, threaded=True)